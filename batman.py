import time
import random
from random import randint

print('Weapon destroyed...')
time.sleep(1)
print('Motion Tracker offline...')
time.sleep(1)
print('\nService Port avaliable...')
from batsay import *
longstring
print('''\n\nYou are special agent Batson, enemy Hawks have infiltrated your base.. you are the last known survivor. 
Save this place, Batson''')

def start(inventory):
	print('\n----------')
	time.sleep(1)
	print('\n[-MAIN ELEVATOR-]')
	print('\n1.) Deck 1 - Security')
	print('2.) Deck 2 - Maintenance')
	print('3.) Deck 3 - Cargo Hold - Airlock')
	print('4.) Deck 4 - Droid Hangar')
	print('5.) Deck 5 - Shuttle Control')
	print('6.) Deck 6 - Observation\n')
	
	cmdlist = ['1', '2', '3', '4', '5', '6',]
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		security(inventory)
	elif cmd == '2':
		if 'droid hack' in inventory:
			print('\n- DECK 2 - MAINTENANCE LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			maintenance(inventory)
	elif cmd == '3':
		cargo_hold(inventory)
	elif cmd == '4':
		if 'laser' in inventory:
			print('\n- DECK 4 - DROID HANGAR LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			droid_hangar(inventory)
	elif cmd == '5':
		shuttle_control(inventory)
	elif cmd == '6':
		if 'motion tracker' in inventory:
			print('\n- DECK 6 - OBSERVATION LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			observation(inventory)
		
def maintenance(inventory):
	print('....')
	time.sleep(1)
	print('''\nThis is the maintenance deck and it appears deserted. 
You see a fallen Bat ally, he has sustained
severe injuries.''')
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
	print('''\nYour fallen friend has a hacking program and it is still in tact,
take it by activating service port
Type service port.''')
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
			print('\nYou now have the hacking ability and return')
			print('to the Main Elevator.')
			time.sleep(2)
			start(inventory)
	elif cmd == '1':
			maintenance(inventory)
	else:
		print('\n error. invalid command-')
	
def cargo_hold(inventory):
	print('\n----------')
	time.sleep(1)
	print('''\nYou enter the Cargo Hold, two Enemy Hawks immediately fire upon you are you are hit!''')
	print('\n[-CARGO HOLD - AIRLOCK-]')
	print('....')
	time.sleep(1)
	print('\nGAME OVER\n')
	exit(0)
	
def droid_hangar(inventory):
	print('....')
	time.sleep(1)
	print('''\nThe Hangar is filled with bodies and debris. The walls are lined in bullets.
Dead hawks and bats lay all around. You see a fallen comrade and can take his weapon, if you can unlock it\n''')
	print('[-DROID HANGAR-]')
	print('\n1.) Fallen Bat access code')
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
		
def repair_droid(inventory, items=['laser']):
	print('\n\n----------')
	print('....')
	time.sleep(1)
	print('Weapon Unlocked.')
	time.sleep(1)
	print('''\nThe weapon is now unlocked. You MUST use serverport to
take the weapon from him safely.''')

	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('laser')
			items = ['laser']
			print('\nLASER ONLINE.')
			print('''\nYou now have a weapon. You lay your fallen friend to rest''')
			time.sleep(2)
			start(inventory)
	else:
		print('\n error. invalid command-')
		
def security(inventory) :
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
			print('\ninitiating hack....')
			time.sleep(2)
			print('....')
			time.sleep(2)
			print('Accessing encrypted files...')
			time.sleep(2)
			print('Decrypting....')
			time.sleep(2)
			print('\n\n[-SEN343 LOG-]')
			time.sleep(1)
			print('\n\nDAILY OVER-RIDE CODES- HANGAR Bats')
			time.sleep(1)
			print('\n\n-Combat Bats - szb41ee')
			time.sleep(1)
			print('\n\n-Sentry Bats - qr66mop')
			time.sleep(1)
			print('\n\n-Weapon Bats - yu8xxj3')
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
	print('1.) Terminate Enemy Hawk')
	print('2.) Retreat to Main Elevator.')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		if 'laser' in inventory:
			print('target locked...')
			time.sleep(1)
			print('...')
			time.sleep(1)
			print('\nTARGET DOWN\n')
			enemy_sentry(inventory)
		else:
			print('\n- WARNING WEAPON IS DOWN -')
			time.sleep(2)
			print('''\nThe Hawk's gun is now active and has you locked
on. You try to run but it is too late..''')
			print('....')
			time.sleep(1)
			print('\nGAME OVER\n')
			exit(0)
			
	elif cmd == '2':
			print('''\nYou try to retreat, but you have no time. You are gunned down before reaching
the elevator''')
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
			print('Activating Motion Tracker...')
			time.sleep(1)
			print('\nMOTION TRACKER ONLINE.')
			time.sleep(2)
			print('''\nYour Motion Tracker is now online.
You return to the main elevator''')
			start(inventory)
			
def shuttle_control(inventory):
	print('''\nYou enter Shuttle Control where all navigation takes place.
Stephen Hawking himself is posted here.
This Man is extremely powerfull.''')
	print('\n[-SHUTTLE CONTROL-]')
	print('\n1.) Attack Hawking')
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
			print('\nEECD999:>')
			print('\n100101010101010101010101010101010' * 10)
			time.sleep(1)
			print('''\nStephen Hawking throws a long and slow laugh
at your pathetic attempt. The last thing your data recorder gets is the
deafing sound of a Target Lock.''')
			print('....')
			print('\nGAME OVER\n')
			exit(0)
	elif cmd == '2':
		start(inventory)
		
def command_droid(inventory):
	print('\nRunning hack...')
	time.sleep(1)
	print('\njamming Auto-Aim...')
	time.sleep(1)
	print('\n......')
	time.sleep(1)
	print('\nMotion Tracker active...')
	time.sleep(1)
	print('\nTracking motion of Hawk...')
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
	print('''\n\nYou have defeated the Stephen and taken back control
of the 'Batcave'. You have saved it from destruction. Reinforcements are inbound.
\n - GAME OVER -\n''')

def getcmd(cmdlist):
	cmd = input('\nCTRL866:> ')
	if cmd in cmdlist:
		return cmd
	elif cmd == 'help':
		print('\nTYPE: inventory to view items')
		print('or quit to self-destruct')
		return getcmd(cmdlist)
	elif cmd == 'inventory':
		print('\ninventory contains:\n')
		for item in inventory:
			print('-- %s' % (item))
		return getcmd(cmdlist)
	elif cmd == 'quit':
		exit(0)
	else:
		print('\n   error. invalid command-\n')
		return getcmd(cmdlist)
	
if __name__ == "__main__":
	inventory = ['service port']
	start(inventory)
