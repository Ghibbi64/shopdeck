from mitmproxy import ctx, http
from datetime import datetime, timezone

# This addon intercepts a specific request and returns a forced XML response.
time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+0000")
POLICYLIST_XML = f"""\
<PolicyList>
\t<MajorVersion>3</MajorVersion>
\t<MinorVersion>0</MinorVersion>
\t<ListId>1892</ListId>
\t<DefaultStop>false</DefaultStop>
\t<ForceVersionUp>true</ForceVersionUp>
\t<UpdateTime>{time}</UpdateTime>
\t<Priority>
\t\t<TitleId>0004003000008f02</TitleId>
\t\t<TaskId>basho0</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>000400300000bc00</TitleId>
\t\t<TaskId>OlvNotf</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>000400300000bd00</TitleId>
\t\t<TaskId>OlvNotf</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>000400300000be00</TitleId>
\t\t<TaskId>OlvNotf</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>0004003000008f02</TitleId>
\t\t<TaskId>pl</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>0004013000003400</TitleId>
\t\t<TaskId>sprelay</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>0004001000021900</TitleId>
\t\t<TaskId>G_ALTASK</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>0004001000022900</TitleId>
\t\t<TaskId>G_ALTASK</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
\t<Priority>
\t\t<TitleId>0004001000020000</TitleId>
\t\t<TaskId>G_ALTASK</TaskId>
\t\t<Level>HIGH</Level>
\t\t<Persistent>true</Persistent>
\t\t<Revive>true</Revive>
\t</Priority>
</PolicyList>"""

from mitmproxy import ctx, http

POLICY_URL_PREFIXES = {
    "https://nppl.c.app.nintendowifi.net/p01/policylist/3/",
}

def request(flow: http.HTTPFlow) -> None:
    try:
        url = flow.request.pretty_url
    except Exception:
        url = flow.request.url

    if any(url.startswith(prefix) for prefix in POLICY_URL_PREFIXES):
        ctx.log.info(f"[POLICY INTERCEPT] Forcing XML response for {url}")
        headers = {"Content-Type": "application/xml; charset=utf-8"}
        flow.response = http.Response.make(200, POLICYLIST_XML, headers)