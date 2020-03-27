# 2-Pass-Assembler-Implementaion
Two pass translation
• Two pass translations consist of pass I and pass II.
• Generally, LC processing performed in the first pass and symbols
defined in the program entered into the symbol table, hence first pass
performs analysis of the source program.
• So, two pass translation of assembly lang. the program can handle
forward reference easily.
• The second pass synthesizes the target form using the address
information found in the symbol table.
• Moreover, The first pass constructs an intermediate representation of
the source program and that will be used by the second pass.
• IR consists of two main components: data structure + IC (intermediate
code)
