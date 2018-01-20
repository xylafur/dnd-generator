
import random

# functions
def read_names(path_to_names='./assets/names.txt'):
    character_names = []
    with open(path_to_names) as names:
        character_names.extend(names.readline().split())
    return character_names

def name_elf(gender):
    """ returns an elf name """
    elf_male_1 = [
    "Ad","Ae","Bal","Bei","Car","Cra","Dae","Dor","El","Ela",
    "Er","Far","Fen","Gen","Glyn","Hei","Her","Ian","Ili","Kea",
    "Kel","Leo","Lu","Mira","Mor","Nae","Nor","Olo","Oma","Pa",
    "Per","Pet","Qi","Qin","Ralo","Ro","Sar","Syl","The","Tra",
    "Ume","Uri","Va","Vir","Waes","Wran","Yel","Yin","Zin","Zum"]

    elf_male_2 = [
    "balar","beros","can","ceran","dan","dithas","faren","fir","geiros","golor",
    "hice","horn","jeon","jor","kas","kian","lamin","lar","len","maer",
    "maris","menor","myar","nan","neiros","nelis","norin","peiros","petor",
    "qen","quinal","ran","ren","ric","ris","ro","salor","sandoral","toris",
    "tumal","valur","ven","warin","wraek","xalim","xidor","yarus","ydark",
    "zeiros","zumin"]

    elf_fem_1 = [
    "Ad","Ara","Bi","Bry","Cai","Chae","Da","Dae","Eil","En",
    "Fa","Fae","Gil","Gre","Hele","Hola","Iar","Ina","Jo","Key",
    "Kris","Lia","Lora","Mag","Mia","Neri","Ola","Ori","Phi","Pres",
    "Qi","Qui","Rava","Rey","Sha","Syl","Tor","Tris","Ula","Uri",
    "Val","Ven","Wyn","Wysa","Xil","Xyr","Yes","Ylla","Zin","Zyl"]

    elf_fem_2 = [
    "banise","bella","caryn","cyne","di","dove","fiel","fina","gella","gwyn",
    "hana","harice","jyre","kalyn","krana","lana","lee","leth","lynn","moira",
    "mys","na","nala","phine","phyra","qirelle","ra","ralei","rel","rie",
    "rieth","rona","rora","roris","satra","stina","sys","thana","thyra","tris",
    "varis","vyre","wenys","wynn","xina","xisys","ynore","yra","zana","zorwyn"]

    nm1, nm2 = (elf_fem_1, elf_fem_2) if gender else (elf_male_1, elf_male_2)
    return random.choice(nm1) + random.choice(nm2)


def name_dwarf(gender):
    """ returns an dwarf name """
    dwarf_male_1 = [
    "Ad","Am","Arm","Baer","Daer","Bal","Ban","Bar","Bel","Ben",
    "Ber","Bhal","Bhar","Bhel","Bram","Bran","Brom","Brum","Bun","Dal",
    "Dar","Dol","Dul","Eb","Em","Erm","Far","Gal","Gar","Ger",
    "Gim","Gral","Gram","Gran","Grem","Gren","Gril","Gry","Gul","Har",
    "Hjal","Hjol","Hjul","Hor","Hul","Hur","Kar","Khar","Kram","Krom",
    "Krum","Mag","Mal","Mel","Mor","Muir","Mur","Rag","Ran","Reg",
    "Rot","Thal","Thar","Thel","Ther","Tho","Thor","Thul","Thur","Thy",
    "Tor","Ty","Um","Urm","Von"]

    dwarf_male_2 = [
    "adin","bek","brek","dahr","dain","dal","dan","dar","dek","dir",
    "dohr","dor","drak","dram","dren","drom","drum","drus","duhr","dur",
    "dus","garn","gram","gran","grim","grom","gron","grum","grun","gurn",
    "gus","iggs","kahm","kam","kohm","kom","kuhm","kum","kyl","man",
    "mand","mar","mek","miir","min","mir","mond","mor","mun","mund",
    "mur","mus","myl","myr","nam","nar","nik","nir","nom","num",
    "nur","nus","nyl","rak","ram","ren","rig","rigg","rik","rim",
    "rom","ron","rum","rus","ryl","tharm","tharn","thran","thrum","thrun"]

    dwarf_fem_1 = [
    "An","Ar","Baer","Bar","Bel","Belle","Bon","Bonn","Braen","Bral",
    "Bralle","Bran","Bren","Bret","Bril","Brille","Brol","Bron","Brul","Bryl",
    "Brylle","Bryn","Bryt","Byl","Bylle","Daer","Dear","Dim","Ed","Ein",
    "El","Gem","Ger","Gwan","Gwen","Gwin","Gwyn","Gym","Ing","Jen",
    "Jenn","Jin","Jyn","Kait","Kar","Kat","Kath","Ket","Las","Lass",
    "Les","Less","Lyes","Lys","Lyss","Maer","Maev","Mar","Mis","Mist",
    "Myr","Mys","Myst","Naer","Nal","Nas","Nass","Nes","Nis","Nys",
    "Raen","Ran","Red","Reyn","Run","Ryn","Sar","Sol","Tas","Taz",
    "Tis","Tish","Tiz","Tor","Tys","Tysh"]

    dwarf_fem_2 = [
    "belle","bera","delle","deth","dielle","dille","dish","dora","dryn","dyl",
    "giel","glia","glian","gwyn","la","leen","leil","len","lin","linn",
    "lyl","lyn","lynn","ma","mera","mora","mura","myl","myla","nan",
    "nar","nas","nera","nia","nip","nis","niss","nora","nura","nyl",
    "nys","nyss","ra","ras","res","ri","ria","rielle","rin","ris",
    "ros","ryl","ryn","sael","selle","sora","syl","thel","thiel","tin",
    "tyn","va","van","via","vian","waen","win","wyn","wynn"]

    nm1, nm2 = (elf_fem_1, elf_fem_2) if gender else (elf_male_1, elf_male_2)
    return random.choice(nm1) + random.choice(nm2)


def name_orc(gender):
    """ returns an orc name """
    nm1 = ["","","","b","bh","br","d","dh","dr","g","gh","gr","j","l","m","n",
           "r","rh","sh","z","zh"]
    nm2 = ["a","o","u"]
    nm3 = ["b","br","bz","d","dd","dz","dg","dr","g","gg","gr","gz","gv","hr",
           "hz","j","kr","kz","m","mz","mv","n","ng","nd","nz","r","rt","rz",
           "rd","rl","rz","t","tr","v","vr","z","zz"]
    nm4 = ["b","d","g","g","k","k","kk","kk","l","ll","n","r"]

    nm5 = ["","","","","b","bh","d","dh","g","gh","h","k","m","n","r","rh","s",
           "sh","v","z"]
    nm6 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e",
           "i","o","u","a","e","i","o","u","a","e","i","o","u","ee","au","ye",
           "ie","aa","ou","ua","ao"]
    nm7 = ["d","dd","dk","dg","dv","g","gg","gn","gv","gz","l","ll","lv","lz",
           "m","md","mz","mv","ng","nk","ns","nz","t","thr","th","v","vn","vr",
           "vg","vd","wnk","wg","wn"]
    nm8 = ["","","","","","f","h","k","l","m","n","ng","v","z"]


    if gender:
        return random.choice(nm5) + random.choice(nm6) + random.choice(nm7) +\
               random.choice(nm6) + random.choice(nm8)
    else:
        return random.choice(nm1) + random.choice(nm2) + random.choice(nm3) +\
                random.choice(nm2) + random.choice(nm4)


def generate_name(race, gender):
    """
        This function takes in a string @race
        and a int gender(0 for male, 1 for female)
        and generates a name.
    """
    assert(type(race) == str and type(gender) == int)
    race_pair = {
        'elf': name_elf,
        'dwarf': name_dwarf,
        'orc': name_orc,
    }
    if race not in race_pair:
        print('Race '+race+' is not a supported race.')
        return 'no-name'

    return race_pair[race](gender)




