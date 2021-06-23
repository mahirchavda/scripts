import pytest

script_name = "splunk_alias"

params_list = [
    {"splunk_home": "", "alias_suffix": ""},
    {"splunk_home": "/opt/splunk2", "alias_suffix": ""},
    {"splunk_home": "/opt/splunk2", "alias_suffix": "2"},
]

actual_params_list = [
    {"splunk_home": "/opt/splunk", "alias_suffix": ""},
    {"splunk_home": "/opt/splunk2", "alias_suffix": ""},
    {"splunk_home": "/opt/splunk2", "alias_suffix": "2"},
]

output = """
### START {script_name}
# Make Splunk CLI Commands Shorter
sp{alias_suffix}_home="{splunk_home}"
export sp{alias_suffix}_home
alias sp{alias_suffix}="$sp{alias_suffix}_home/bin/splunk"
alias log{alias_suffix}="cd $sp{alias_suffix}_home/var/log/splunk"
alias modinput{alias_suffix}="cd $sp{alias_suffix}_home/var/lib/splunk/modinputs"
alias app{alias_suffix}="cd $sp{alias_suffix}_home/etc/apps"
alias rr{alias_suffix}="sp{alias_suffix} restart"
alias sclean{alias_suffix}="sp{alias_suffix} clean eventdata -f"
alias ssclean{alias_suffix}="sp{alias_suffix} stop && sclean{alias_suffix} && sp{alias_suffix} start"
alias sssclean{alias_suffix}="sp{alias_suffix} stop && sclean{alias_suffix} && log{alias_suffix} && rm -rf * && modinput{alias_suffix} && rm -rf * && sp{alias_suffix} start"
### END {script_name}
"""


@pytest.mark.parametrize("params,actual_params", zip(params_list, actual_params_list))
def test_splunk_alias(app, client, params, actual_params):
    res = client.get(
        "/{script_name}".format(script_name=script_name), query_string=params
    )
    assert res.status_code == 200
    res_cmds = res.get_data().decode().strip("\n").splitlines()
    actual_cmds = (
        output.format(script_name=script_name, **actual_params).strip("\n").splitlines()
    )
    assert res_cmds == actual_cmds
