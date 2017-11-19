# rlm_aprsis
Freeradius python module for dynamic APRS-IS Passcode generation

This python module has been built to enable dynamic APRS-IS passcode generation on freeradius 3.0.11 (and higher). 

It's used to build a Wi-Fi network architecture similar to [Eduroam](https://www.eduroam.org), for ham radio operators, leveraging the existing APRS-IS passcode authentication. 

To use `rlm_aprsis`, copy `aprsis.py` in `/etc/freeradius/3.0/mods-config/python`, and edit `/etc/freeradius/3.0/mods-available/python` as follow:

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

A more complete configuration guide will be shipped here later (when it's done).

