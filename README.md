# Scripts
This project provides API endpoints to get my often-used scripts.

Hosted on HEROKU: https://scripts-mahirchavda.herokuapp.com/

## Endpoints:

### Script Endpoint: https://scripts-mahirchavda.herokuapp.com/script/<script_name>

Currently available script_names are:
* [install_miniconda](#install_miniconda)
* [splunk_alias](#splunk_alias)

---

#### install_miniconda: https://scripts-mahirchavda.herokuapp.com/script/install_miniconda
* returns the bash commands to install miniconda

Example to install miniconda
```bash
curl https://scripts-mahirchavda.herokuapp.com/script/install_miniconda | bash
```


#### splunk_alias: https://scripts-mahirchavda.herokuapp.com/script/splunk_alias
* returns the alias for often used splunk cli commands

To configure the alias run below command in your linux shell:
```bash
curl 'https://scripts-mahirchavda.herokuapp.com/script/splunk_alias' >> ~/.bashrc && source ~/.bashrc
```

Splunk cli commands and it's alias

| Purpose | Splunk CLI command | Splunk alias |
|---------|--------------------|--------------|
| Restart Splunk | /opt/splunk/bin/splunk restart	| rr |
| Start/Stop/Restart Splunk | /opt/splunk/bin/splunk start/stop/restart |	sp start/stop/restart |
| cd into the Splunk apps folder | cd /opt/splunk/etc/apps | app |
| cd into the Splunk log folder |	cd /opt/splunk/var/log/splunk	| log |
| cd into Splunk modinput folder | cd /opt/splunk/var/lib/splunk/modinputs	| modinput |
| To clean all the indexed we have to perform below step: <br/>1) stop splunk<br/>2) clean indexes data<br/>3) start splunk | 1) /opt/splunk/bin/splunk stop<br/>2) /opt/splunk/bin/splunk clean eventdata -f<br/>3) /opt/splunk/bin/splunk start | ssclean |
| To just clean eventdata | /opt/splunk/bin/splunk clean eventdata -f | sclean |
| 1) Stop Splunk<br/>2) Navigate to the Splunk log folder<br/>3) Delete all files and folder<br/>4) Navigate to the Splunk modinput folder<br/>5) Delete all files and folder<br/>6) Clean all the indexed data<br/>7) Navigate to the Splunk apps folder<br/>8) Remove Splunk_TA_cisco-ucs app<br/>9) Start Splunk | 1) /opt/splunk/bin/splunk stop<br/>2) cd /opt/splunk/var/log/splunk<br/>3) rm -rf *<br/>4) cd /opt/splunk/var/lib/splunk/modinputs<br/>5) rm -rf *<br/>6) /opt/splunk/bin/splunk clean eventdata -f<br/>7) cd /opt/splunk/etc/apps<br/>8) rm -rf Splunk_TA_cisco-ucs<br/>9) /opt/splunk/bin/splunk start | sp stop && log && rm -rf * && modinput && rm -rf * && sclean && app && rm -rf Splunk_TA_cisco-ucs && sp start |


The splunk_alias endpoint also supports two parameters: **splunk_home** and **alias_suffix**
| param | default value | description |
|-------|---------------|-------------|
| splunk_home | "/opt/splunk" | specify splunk home path |
| alias_suffix | "" | specify suffix if you have mulitple splunk installed and you want to configure splunk alias for both the splunk |

Example:
```bash
$ curl 'https://scripts-mahirchavda.herokuapp.com/script/splunk_alias?splunk_home=/opt/splunk2&alias_suffix=2'
# output:
### START splunk_alias
# Make Splunk CLI Commands Shorter
sp2_home="/opt/splunk2"
export sp2_home
alias sp2="$sp2_home/bin/splunk"
alias log2="cd $sp2_home/var/log/splunk"
alias modinput2="cd $sp2_home/var/lib/splunk/modinputs"
alias app2="cd $sp2_home/etc/apps"
alias rr2="sp2 restart"
alias sclean2="sp2 clean eventdata -f"
alias ssclean2="sp2 stop && sp2 clean eventdata -f && sp2 start"
### END splunk_alias
```
