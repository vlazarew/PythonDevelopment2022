import cmd

from pynames.generators import scandinavian, russian, mongolian, korean, goblin, orc
from pynames.generators.elven import *
from pynames.generators.iron_kingdoms import *


class NamesGenerator(cmd.Cmd):
    simple_generators = {'scandinavian': scandinavian.ScandinavianNamesGenerator,
                         'russian': russian.PaganNamesGenerator,
                         'mongolian': mongolian.MongolianNamesGenerator,
                         'korean': korean.KoreanNamesGenerator,
                         'goblins': goblin.GoblinGenerator,
                         'orcs': orc.OrcNamesGenerator}
    elven_generators = {'warhammer': WarhammerNamesGenerator,
                        'dnd': DnDNamesGenerator}
    iron_kingdoms_generators = {'caspian_midlunder_sulese': CaspianMidlunderSuleseFullnameGenerator,
                                'dwarf': DwarfFullnameGenerator,
                                'gobber': GobberFullnameGenerator,
                                'iossan_nyss': IossanNyssFullnameGenerator,
                                'khadoran': KhadoranFullnameGenerator,
                                'orgun': OgrunFullnameGenerator,
                                'ryn': RynFullnameGenerator,
                                'thurian_morridane': ThurianMorridaneFullnameGenerator,
                                'tordoran': TordoranFullnameGenerator,
                                'trollkin': TrollkinFullnameGenerator}


NamesGenerator().cmdloop()
