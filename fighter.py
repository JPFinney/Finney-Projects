import time
import random
from random import randint
print("Missing gun")
time.sleep(1)
print("Tracker broken")
time.sleep(1)
print("Bat Awoken")
time.sleep(1)
from batsay import *
longstring
print("You are special agent Batson, enemy hawks have infiltrated your base... you are the last known survivor.")
def start(inventory):
	print('\n----------')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\n1.) deck 1 - Security')
	print('2.) deck 2 - Maintenance')
	print('3.) deck 3 - Cargo Hold - Airlock')
	print('4.) deck 4 - Droid Hangar')
	print('5.) deck 5 - Shuttle Control')
	print('6.) deck 6 - Observation')
	
	cmdlist = ['1', '2', '3', '4', '5', '6',]
	cmd = (cmdlist)
	
	if cmd == '1':
		security(inventory)
	elif cmd == '2':
		if 'bathack' in inventory:
			print('\n- DECK 2 - MAINTENANCE LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			maintenance(inventory)
	elif cmd == '3':
		cargo_hold(inventory)
	elif cmd == '4':
		if 'laser' in inventory:
			print('\n- DECK 4 - HANGAR LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			bat_hangar(inventory)
	elif cmd == '5':
		shuttle_control(inventory)
	elif cmd == '6':
		if 'tracker' in inventory:
			print('\n- DECK 6 - OBSERVATION LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			observation(inventory)
		
def maintenance(inventory):
	print('''\nThis is the maintenance deck and it appears deserted. 
You see a fallen comrade, he is riddled with bullets.''')
	print('\n[-MAINTENANCE-]\n')
	print('1.) Dead Bat')
	print('2.) Return to Main Elevator\n')

	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	if cmd == '1':
		crew_droid(inventory)
	elif cmd == '2':
		start(inventory)
		
def crew_droid(inventory, items=['droid hack']):
	print('\n----------')
	print('''\nFallen Bat has a hacking program and it's connection
outlet is still intact. You can connect to it with service
port and download the program.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
			print('\n\n1.) Exit.')
	cmdlist = ['service port', '1']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('droid hack')
			items = ['droid hack']
			print('\nservice port connected.')
			time.sleep(1)
			print('accessing file..')
			time.sleep(1)
			print('downloading..')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\ndownload complete.')
			print('to the Main Elevator.')
			time.sleep(2)
			start(inventory)
	elif cmd == '1':
			maintenance(inventory)
	else:
		print('\n error. invalid command-')
def cargo_hold(inventory):
	print('....')
	time.sleep(1)
	print('''\nYou enter the Cargo Hold, two Enemy Hawks
unload on you. Their fire is accurate
and you take a direct hit.''')
	print('\n[-CARGO HOLD - AIRLOCK-]')
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\nDeath imminent...')
	time.sleep(1)
	print('\nGAME OVER\n')
	exit(0)
	
def droid_hangar(inventory):
	print('\n----------')
	print('....')
	time.sleep(1)
	print('''\nThe Hangar is filled with debri. There
are bullet holes everywhere and the floor is covered in bodies of hawks and bats.
In the corner there is one dead bat with a weapon you can retrieve. You need the access code to unlock it.\n''')
	print('[-HANGAR-]')
	print('\n1.) Repair Bat Code')
	print('2.) Return to Main Elevator')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		access_code(inventory)
	elif cmd == '2':
		start(inventory)
		
def access_code(inventory):
	code = '%d%d%d' % (randint(0,9), randint(0,9), randint(0,9))
	guess = input('\n[KEYPAD]> ')
	guesses = 0
	
	while guess != code and guess != 'yu8xxj3' and guesses <4:
		print('\n* ACCESS - DENIED *')
		guesses += 1
		guess = input('\n[KEYPAD]> ')
		
	if guess == code or guess == 'yu8xxj3':
		repair_droid(inventory)
	else:
		print('\n....')
		time.sleep(1)
		print('\n....')
		time.sleep(1)
		print('\nKEYPAD - LOCKED')
		time.sleep(1)
		print('\ncode randomizing..')
		time.sleep(1)
		print('\nKEYPAD - OPEN')
		time.sleep(1)
		droid_hangar(inventory)
def repair_droid(inventory, items=['gun']):
	print('Unlocking Weapon....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('Weapon Unlocked.')
	time.sleep(1)
	print('''\nThe gun is now active. You MUST connect to with service port to aquire weapon.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('laser')
			items = ['laser']
			print('\nservice port connected.')
			time.sleep(1)
			print('Taking Gun...')
			time.sleep(1)
			print('Auto alignment...')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\nWEAPON LOADED.')
			start(inventory)
	else:
		print('\n error. invalid command-')
def security(inventory):
	print('\n----------')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou are on the Security Deck. This is where all
surveillance is done. Recorder Bat has been
terminated. You MUST access his logs but you
will have to hack his data recorder.\n''') 
	print('[-SECURITY-]\n')
	print('1.) View Surveillance monitors on other decks')
	print('2.) Hack Recorder Bat Logs')
	print('3.) Return to main elevator')
	
	cmdlist =['1', '2', '3']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		print('\n----------')
		print('\nBooting Monitors....')
		time.sleep(1)
		print('....')
		time.sleep(1)
		print('...')
		time.sleep(1)
		print('Monitors active.')
		time.sleep(1)
		print('\n[-SURVEILLANCE FEED-]')
		print('''\n-The Hangar monitor is offline you have no live feed.
\n-In the Cargo hold there are two Hawks searching for enemies.
\n-The Maintenance deck looks clear except for a few terminated bats.
\n-An Elite Enemy Command Hawk is posted on the Shuttle Control deck.
\n-Observation shows an Enemy Hawk.''')
		time.sleep(2)
		security(inventory)
	elif cmd == '2':
		if 'droid hack' in inventory:
			print('\nloading hack....')
			time.sleep(2)
			print('....')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('Accessing encrypted files...')
			time.sleep(2)
			print('Decrypting....')
			time.sleep(2)
			print('\n\n[-SEN343 LOG-]')
			time.sleep(1)
			print('\n\nDAILY OVER-RIDE CODES- HANGAR DROIDS')
			time.sleep(1)
			print('\n\n-Combat Bats - szb41ee')
			time.sleep(1)
			print('\n\n-Sentry Bats - qr66mop')
			time.sleep(1)
			print('\n\n-Repair Bats - yu8xxj3')
			time.sleep(1)
			print('\n\nCODES WILL BE RESET EVERY 24 HOURS')
			security(inventory)
		else:
			print('\n- ACCESS TO DATA RECORDER DENIED -')
			time.sleep(2)
			security(inventory)
	elif cmd == '3':
		start(inventory)
		
def observation(inventory):
	print('....')
	time.sleep(1)
	print('''\nYou enter the Observation deck and are confronted 
with an Enemy Hawk beside a dead bat. 
His weapon is almost ready and will be active in seconds.\n''')
	print('[-OBSERVATION-]\n')
	print('1.) Terminate Hawk')
	print('2.) Retreat to Main Elevator.')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		if 'laser' in inventory:
			print('\nTARGET TERMINATED\n')
			enemy_sentry(inventory)
		else:
			print('\n- WARNING GUN OFFLINE -')
			time.sleep(2)
			print('''\nThe Hawk's gun is now active and has you locked
on. You try to hide but it is too late..''')
			print('....')
			time.sleep(1)
			print('\nGAME OVER\n')
			exit(0)
			
	elif cmd == '2':
			print('''\nThe Hawk Gun is now active and has you locked
on. You try to retreat back to the elevator but its to late..''')
			print('....')
			time.sleep(1)
			print('\nGAME OVER\n')
			exit(0)
			
def enemy_sentry(inventory, items=['motion tracker']):
	print('\n----------')
	time.sleep(1)
	print('''\nThis Enemy Hawk has been terminated. 
Judging by the ranking on his chest you know he has a
motion tracker. You MUST connect 
to it with service port and download the program.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('motion tracker')
			items = ['motion tracker']
			print('\nservice port connected.')
			time.sleep(1)
			print('\nMOTION TRACKER ONLINE.')
			time.sleep(2)
			print('''\nYour Motion Tracker is now online.
You return to the main elevator''')
			start(inventory)
			
def shuttle_control(inventory):
	print('\n----------')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou enter Shuttle Control where all navigation takes place.
A 999 Elite Enemy Command Hawk is posted here.
This Hawk is extremely powerfull.''')
	print('\n[-SHUTTLE CONTROL-]')
	print('\n1.) Terminate the 999 Elite Enemy Command Hawk')
	print('2.) Retreat to Main Elevator')
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		if 'laser' in inventory and 'motion tracker' in inventory and 'droid hack' in inventory:
			print('\n....')
			time.sleep(1)
			print('\n....')
			command_droid(inventory)
		else:
			time.sleep(1)
			print('''\nThe Elite Enemy Command Hawk laughs
at your pathetic attempt. The last thing your data recorder gets is the
deafening sound of a Target Lock.''')
			print('....')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\nGAME OVER\n')
			exit(0)
	elif cmd == '2':
		start(inventory)
		
def command_droid(inventory):
	print('\nRunning hack...')
	time.sleep(1)
	print('\njamming Hawk Lock...')
	time.sleep(1)
	print('\n......')
	time.sleep(1)
	print('\nMotion Tracker active...')
	time.sleep(1)
	print('\nTracking Stephen Hawking...')
	time.sleep(1)
	print('\n......')
	time.sleep(1)
	print('\nWeapon active...')
	time.sleep(1)
	print('\nTargeting Hawk...')
	time.sleep(1)
	print('\nTarget Locked...')
	time.sleep(1)
	print('\n......')
	time.sleep(2)
	print('\n\nTARGET DOWN \n')
	time.sleep(2)
	print('''\n\nYou have defeated the Command Hawk, Stephen Hawking and taken back control
of the 'Batmobile'. The flight path has been restored and
a distress signal sent to Droid Command. Reinforcements are inbound.
\n - GAME OVER -\n''')
if __name__ == "__main__":
	inventory = ['service port']
	start(inventory)
