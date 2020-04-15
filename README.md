# rlm_aprsis
Freeradius module for dynamic APRS-IS Passcode generation

This module has been built to enable dynamic APRS-IS passcode generation on freeradius 3.0.11 (and higher). 

It's used to build a Wi-Fi network architecture similar to [Eduroam](https://www.eduroam.org), for ham radio operators, leveraging the existing APRS-IS passcode authentication. 

## Installing for rlm_python

To use `rlm_aprsis` with the `rlm_python` module, copy `aprsis.py` in `/etc/freeradius/3.0/mods-config/python`, and edit `/etc/freeradius/3.0/mods-available/python` as follow:

```
python {
	module = aprsis
	python_path = ${modconfdir}/${.:name}

	mod_instantiate = ${.module}
	func_instantiate = instantiate

	mod_detach = ${.module}
	func_detach = detach

	mod_authorize = ${.module}
	func_authorize = authorize

	mod_authenticate = ${.module}
	mod_preacct = ${.module}
	mod_accounting = ${.module}
	mod_checksimul = ${.module}
	mod_pre_proxy = ${.module}
	mod_post_proxy = ${.module}
	mod_post_auth = ${.module}
	mod_recv_coa = ${.module}
	mod_send_coa = ${.module}
}
```
Create a soft link of the aforementioned file in `/etc/freeradius/3.0/mods-enabled`.

Edit your site configuration file. In the `authorize` section, add `python` after `preprocess`, but before `chap`, `mschap`, and `pap`.

You should edit your configuration appropriately to enable PEAP-MSCHAPv2.  

## Installing for rlm_perl

To use `rlm_aprsis` with the `rlm_perl` module, copy `aprsis.pl` in `/etc/freeradius/3.0/mods-config/perl`, and edit `/etc/freeradius/3.0/mods-available/perl` as follow:

```
perl {
	filename = ${modconfdir}/${.:instance}/aprsis.pl

	func_authenticate = authenticate
	func_authorize = authorize
	func_detach = detach
}
```
Create a soft link of the aforementioned file in `/etc/freeradius/3.0/mods-enabled`.

Edit your site configuration file. In the `authorize` section, add `perl` after `preprocess`, but before `chap`, `mschap`, and `pap`.

You should edit your configuration appropriately to enable PEAP-MSCHAPv2.  

