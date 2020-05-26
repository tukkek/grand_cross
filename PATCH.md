The provided `project-demi.ips` patch comes from the fantastic [Project Demi](https://projectdemi.com/). However, the original patches were not compatible with the `y` randomizer option ("Randomize jobs obtained from crystal shards"), so I had to remove the cutscene skips for the four crystal rooms to restore compatibility.

Everything else in the game outside of those four crystal rooms should behave exactly as intended by the Project Demi authors if the patch is applied. One unfortunate side effect however is that if you go to the Key Item menu, the objective hint will not update after obtaining the crystals.

For the technically inclined, here are the reproduction steps:

1. Obtain the assembly files from Project Demi (link to specific commit used here is provided in the next step).
2. Navigate to [this particular folder](https://github.com/caerulius/FFVCareerDay/tree/d1afad97bb1231fdb38b05ea61103f3888c22e88/bigbridge-web/projectdemiapi/project_demi/asm) in your local working tree.
3. In `all_patches.asm`, disable the following: `wind_crystal.asm`, `water_crystal.asm`, `fire_crystal.asm`, `earth_crystal.asm`, and `black_chocobo.asm` by adding a `;` at the start of each line.
4. Rename your ROM to `.sfc` instead of `.smc`, if necessary. The next step will overwrite the input file so you may want to make a copy for that purpose!
5. Generate the patch using [Asar](https://github.com/RPGHacker/asar). The exact command is: `asar --define dash=0 --define learning=0 --define pitfalls=0 --define passages=0 --define double_atb=0 --define boss_exp=0 --fix-checksum=off --define vanillarewards=1 --no-title-check all_patches.asm rom.sfc`.
6. Use [Lipx](https://github.com/kylon/Lipx) to generate an IPS patch (command: `python3 lipx.py -c orignal.smc patched.sfc project-demi.ips`). The resulting IPS should serve to patch ROMs post-randomization with `patcher.py` (see `README` for details).
