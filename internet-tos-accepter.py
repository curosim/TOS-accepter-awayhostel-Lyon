import requests

def accept_tos():
	data = {
		'textfield': 'Welcome to our Internet portal. If you choose to continue, you are agreeing to comply with and be bound by the following terms and conditions of use. If you disagree with any part of these terms and conditions, you may not continue.\r\n\r\nTerms of use:\r\n\r\n1. Your use of any information or materials on sites you access is entirely at your own risk, for which we shall not be liable.\r\n\r\n2. You agree that, though this portal, you will not perform any of the following acts:\r\n\r\n- Attempt to access devices or resources to which you have no explicit, legitimate rights\r\n\r\n- Copy, reproduce, or transmit any copyrighted files or information other than in accordance with the requirements and allowances of the copyright holder\r\n\r\n- Launch network attacks of any kind including port scans, DoS/DDoS, packet floods, replays or injections, session hijacking or interception, or other such activity with malicious intent\r\n\r\n- Transmit malicious software such as viruses, Trojan horses, and worms\r\n\r\n- Surreptitiously install software or make configuration changes to any device or application, by means of the installation or execution of key loggers, registry keys,  or other executable or active application or script\r\n\r\n3. You agree that you will use the access provided here responsibly and with full regard to the safety, security, and privacy of all other users, devices, and resources. \r\n\r\n4. You agree that you will be mindful of the cultural sensitivities of others while using this portal so as not to provoke reaction or offense, and that you will not intentionally access pornographic, graphically violent, hateful, or other offensive material (as deemed by us) regardless of others´ sensitivities.\r\n\r\n5. You understand that we reserve the right to log or monitor traffic to ensure that these terms are being followed.\r\n\r\n6. You understand that unauthorized use of resources through this portal may give rise to a claim for damages and/or be a criminal offense.\r\n\r\n\t\t\t\t',
		'checkbox': 'checkbox',
		'Submit': 'Accept',
	}
	response = requests.post('http://198.18.34.1/reg.php', data=data)
	return response.text

def main():
	print("[*] Trying to accept TOS and establishing Internet connection...")
	resp = accept_tos()

	if "now connected" in resp: print("[*] TOS accepted successfully! Internet should work now :)")
	else: print("[!] Failed to accept TOS. Does Internet work?")


main()
