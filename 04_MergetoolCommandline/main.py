import cmd
import shlex

from pynames.generators import scandinavian, iron_kingdoms, elven, orc, goblin, korean, mongolian, russian


class NamesGenerator(cmd.Cmd):
    gens = {
        'scandinavian': {'traditional': scandinavian.ScandinavianNamesGenerator()},
        'russian': {'pagan': russian.PaganNamesGenerator()},
        'mongolian': {'traditional': mongolian.MongolianNamesGenerator()},
        'korean': {'traditional': korean.KoreanNamesGenerator()},
        'goblin': {'custom': goblin.GoblinGenerator()},
        'orc': {'custom': orc.OrcNamesGenerator()},
        'elven': {
            'dnd': elven.DnDNamesGenerator(),
            'warhammer': elven.WarhammerNamesGenerator(),
        },
        'iron_kingdoms': {
            'caspian_midlunder_sulese': iron_kingdoms.CaspianMidlunderSuleseFullnameGenerator(),
            'dwarf': iron_kingdoms.DwarfFullnameGenerator(),
            'gobber': iron_kingdoms.GobberFullnameGenerator(),
            'iossan_nyss': iron_kingdoms.IossanNyssFullnameGenerator(),
            'khadoran': iron_kingdoms.KhadoranFullnameGenerator(),
            'ogrun': iron_kingdoms.OgrunFullnameGenerator(),
            'ryn': iron_kingdoms.RynFullnameGenerator(),
            'thurian_morridane': iron_kingdoms.ThurianMorridaneFullnameGenerator(),
            'tordoran': iron_kingdoms.TordoranFullnameGenerator(),
            'trollkin': iron_kingdoms.TrollkinFullnameGenerator(),
        }
    }
    genders = {
        'male': 'm',
        'female': 'f',
    }
    default_gender = genders['male']
    languages = {'ru', 'en'}

    def __init__(self):
        super().__init__()
        self.language = 'native'

    def class_parse(self, args):
        option = None

        class_name, *params = shlex.split(args)
        if len(self.gens[class_name]) == 1:
            subclass = list(self.gens[class_name].keys())[0]
            if len(params) > 0:
                option = params[0]
        else:
            subclass = params[0]
            if len(params) > 1:
                option = params[1]
        return class_name, subclass, option

    def do_generate(self, args):
        try:
            class_name, subclass, option = self.class_parse(args)
            gender = self.default_gender if option is None else self.genders[option]
        except:
            print('generate: incorrect parameters')
            return

        gen = self.gens[class_name][subclass]
        lang = self.language if self.language in gen.languages else gen.native_language
        res = gen.get_name_simple(gender, lang)
        print(res)

    def complete_generate(self, prefix, allcmd, beg, end):
        _, *params = shlex.split(allcmd)
        current = len(params)
        if prefix == '':
            current += 1

        if current == 1:
            variants = self.gens.keys()
        else:
            name = params[0]
            if len(self.gens.get(name, {})) > 1:
                if current == 2:
                    variants = self.gens.get(name, {}).keys()
                elif current == 3:
                    variants = self.genders
            else:
                if current == 2:
                    variants = self.genders
                else:
                    variants = []
        return [cmd for cmd in variants if cmd.startswith(prefix)]

    def do_language(self, args):
        try:
            lang, *_ = shlex.split(args)
            if lang in self.languages:
                self.language = lang
            else:
                raise KeyError
        except:
            print('language: incorrect parameters')

    def complete_language(self, prefix, allcmd, beg, end):
        variants = self.languages
        return [cmd for cmd in variants if cmd.startswith(prefix)]

    def do_info(self, args):
        try:
            class_name, subclass, option = self.class_parse(args)
        except:
            print('info: incorrect parameters')
            return

        gen = self.gens[class_name][subclass]

        if option in self.genders:
            print(gen.get_names_number(self.genders[option]))
        elif option == 'language':
            print(*gen.languages)
        elif option is None:
            print(gen.get_names_number())
        else:
            print('info: incorrect parameters')

    def complete_info(self, prefix, allcmd, beg, end):
        _, *params = shlex.split(allcmd)
        current = len(params)
        if prefix == '':
            current += 1

        if current == 1:
            variants = self.gens.keys()
        else:
            name = params[0]
            if len(self.gens.get(name, {})) > 1:
                if current == 2:
                    variants = self.gens.get(name, {}).keys()
                elif current == 3:
                    variants = list(self.genders.keys()) + ['language']
            else:
                if current == 2:
                    variants = list(self.genders.keys()) + ['language']
                else:
                    variants = []
        return [cmd for cmd in variants if cmd.startswith(prefix)]


NamesGenerator().cmdloop()
