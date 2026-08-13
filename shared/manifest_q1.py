# Q1 only files; would not be needed on Mk4
freeze_as_mpy('', [
	'battery.py',
	'bbqr.py',
	'calc.py',
	'decoders.py',
	'gpu.py',
	# kravens: HSM support was Mk4-only (frozen via manifest_mk4). Enabling supports_hsm on the Q
	# for coinjoin remote signing means these must be frozen here too, or flow.py's top-level
	# `from hsm import hsm_policy_available` (and users) raises ImportError on the frozen build and
	# the device wedges after login. The simulator loads from source so it never surfaced this.
	'hsm.py',
	'hsm_ux.py',
	'keyboard.py',
	'lcd_display.py',
	'notes.py',
	'q1.py',
	'scanner.py',
	'st7788.py',
	'teleport.py',
	'users.py',
	'ux_q1.py'
], opt=0)

# Optimize data-like files, since no need to debug them.
freeze_as_mpy('', [
	'font_iosevka.py',
	'gpu_binary.py',        # remove someday?
	'graphics_q1.py',
], opt=3)

