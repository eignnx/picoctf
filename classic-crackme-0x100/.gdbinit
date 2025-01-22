set disassembly-flavor intel
tui layout asm
tui reg general
set logging enabled on

break *main
break *main+500
run
