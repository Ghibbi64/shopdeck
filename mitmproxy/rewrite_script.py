from mitmproxy import ctx, http, connection

# ── Rewrite rules ─────────────────────────────────────────────────────────────
# Each entry: (prefix_to_match, replacement_prefix)
server_ip = "0.0.0.0"
URL_REWRITES = [
    # Nintendo eShop
    ("https://ecs.c.shop.nintendowifi.net",  f"https://{server_ip}:8000"),
    ("https://ninja.ctr.shop.nintendo.net",  f"https://{server_ip}:9000"),
    ("https://nus.c.shop.nintendowifi.net",  f"https://{server_ip}:8000"),
    # BOSS/BGM redirect to local server
    #("https://npdl.cdn.nintendowifi.net/p01/nsa/AH3oZwrEbne6qHCO/BGM1/EU_BGM1", f"http://{server_ip}/BOSS/eshop/EU_BGM1"),
]

# ── Hooks ─────────────────────────────────────────────────────────────────────

def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url

    for prefix, replacement in URL_REWRITES:
        if url.startswith(prefix):
            new_url = replacement + url[len(prefix):]
            ctx.log.info(f"[rewrite] {url} -> {new_url}")
            flow.request.url = new_url
            break  # only apply the first matching rule

    ctx.log.debug(f"[request] {flow.request.method} {flow.request.pretty_url}")


def client_connected(client_conn: connection.Client) -> None:
    ctx.log.info(f"[client connect] {client_conn.address}")


def server_connected(server_conn: connection.Server) -> None:
    ctx.log.info(
        f"[server connect] address={getattr(server_conn, 'address', None)}"
        f" sni={getattr(server_conn, 'sni', None)}"
    )


def client_connected_failed(server_conn: connection.Server) -> None:
    ctx.log.warn(
        f"[server FAILED] address={getattr(server_conn, 'address', None)}"
        f" sni={getattr(server_conn, 'sni', None)}"
        f" error={getattr(server_conn, 'connection_error', None)}"
    )