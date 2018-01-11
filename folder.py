import os
import glob
import shutil
import re
 
#fromdir = "F:/ani"
fromdir = "./"
os.chdir(fromdir)

list = [[0 for col in range(60)] for row in range(5)]
list[0][0] = "2017-2";
list[0][1] = "Re-Creators";
list[0][2] = "Sagrada Reset";
list[0][3] = "Sakura Quest";
list[0][4] = "Re-Creators";
list[0][5] = "ACCA 13-ku Kansatsu-ka";
list[0][6] = "Alice to Zouroku";
list[0][7] = "Ani ni Tsukeru Kusuri wa Nai!";
list[0][8] = "Berserk 2017";
list[0][9] = "Busou Shoujo Machiavellianism";
list[0][10] = "Clockwork Planet";
list[0][11] = "Dungeon ni Deai o Motomeru no wa Machigatte Iru Darouka Gaiden - Sword Oratoria";
list[0][12] = "Eromanga Sensei";
list[0][13] = "Frame Arms Girl";
list[0][14] = "Fukumenkei Noise";
list[0][15] = "Gin no Guardian";
list[0][16] = "Granblue Fantasy The Animation";
list[0][17] = "Hinako Note";
list[0][18] = "ID-0";
list[0][19] = "Idolmaster Cinderella Girls Gekijou";
list[0][20] = "Renai Boukun";
list[0][21] = "Roku de Nashi Majutsu Koushi to Akashic Records";
list[0][22] = "Saenai Heroine no Sodatekata Flat";
list[0][23] = "Seikaisuru Kado";
list[0][24] = "Shingeki no Bahamut - Virgin Soul";
list[0][25] = "Shingeki no Kyojin Season 2";
list[0][27] = "Sin - Nanatsu no Taizai";
list[0][28] = "Tsugumomo";
list[0][29] = "Tsuki ga Kirei";
list[0][30] = "Uchouten Kazoku 2";
list[0][31] = "Zero kara Hajimeru Mahou no Sho";

list[1][0] = "2017-3";
list[1][1] = "Aho Girl";
list[1][2] = "Isekai wa Smartphone to Tomo ni";
list[1][3] = "Kakegurui";
list[1][4] = "Keppeki Danshi! Aoyama-kun";
list[1][5] = "Konbini Kareshi";
list[1][6] = "Made in Abyss";
list[1][7] = "Netsuzou Trap (NTR)";
list[1][8] = "New Game!!";
list[1][9] = "Nora to Oujo to Noraneko Heart";
list[1][10] = "Orange";
list[1][11] = "Skirt no Naka wa Kedamono Deshita";
list[1][12] = "Shoukoku no Altair";
list[1][13] = "Tsurezure Children";
list[1][14] = "Youkai Apartment no Yuuga na Nichijou";
list[1][15] = "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e";
list[1][16] = "Fate - Apocrypha";
list[1][17] = "18if";
list[1][18] = "Clione no Akari";
list[1][19] = "Dive!!";
list[1][20] = "Gamers!";
list[1][21] = "Hajimete no Gal";
list[1][22] = "Isekai Shokudou";
list[1][23] = "Koi to Uso"; 
list[1][24] = "Idol Jihen";
list[1][25] = "Senki Zesshou Symphogear AXZ";
list[1][26] = "Twin Angel Break";
list[1][27] = "Princess Principal";
list[1][28] = "Tenshi no 3P!";

list[2][0] = "2017-4";
list[2][1] = "Shokugeki no Souma - San no Sara";
list[2][2] = "TsukiPro The Animation";
list[2][3] = "KAme-iro Cocoa Series - Ame-con!!";
list[2][4] = "Two Car";
list[2][5] = "Urahara";
list[2][6] = "Shoujo Shuumatsu Ryokou Special";
list[2][7] = "Taishou Mebiusline - Chicchai-san";
list[2][8] = "Yuuki Yuuna wa Yuusha de Aru - Yuusha no Shou";
list[2][9] = "Taishou Mebiusline - Chicchai-san";
list[2][10] = "Shoujo Shuumatsu Ryokou";
list[2][11] = "Ou-sama Game The Animation";
list[2][12] = "Mahou Tsukai no Yome";
list[2][13] = "Love Live! Sunshine!! 2";
list[2][14] = "Love Kome - We Love Rice Nikisaku";
list[2][15] = "Kekkai Sensen & Beyond";
list[2][16] = "Dia Horizon";
list[2][17] = "Osomatsu-san 2";
list[2][18] = "UQ Holder! Mahou Sensei Negima! 2";
list[2][19] = "Wake Up, Girls! Shin Shou";
list[2][20] = "Blend S";
list[2][21] = "Boku no Kanojo ga Majime Sugiru Shobitch na Ken";
list[2][22] = "Classicaloid";
list[2][23] = "Code Realize - Sousei no Himegimi";
#list[2][24] = "Dia Horizon";
list[2][25] = "Dies Irae";
list[2][26] = "Dream Festival! R";
list[2][27] = "Dynamic Chord";
list[2][28] = "Evil or Live";
list[2][29] = "Gintama (2017) 2nd";
list[2][30] = "Himouto! Umaru-chan R";
list[2][31] = "Houseki no Kuni (2017)";
list[2][32] = "Idolmaster Cinderella Girls Gekijou 2";
list[2][33] = "Imouto sae Ireba Ii";
list[2][34] = "Infini-T Force";
list[2][35] = "Inuyashiki";
list[2][36] = "Juuni Taisen";
list[2][37] = "Kekkai Sensen & Beyond";
list[2][38] = "Kino no Tabi - The Beautiful World - Animated Series";
list[2][39] = "Konohana Kitan";
list[2][40] = "Kujira no Kora wa Sajou ni Utau";
#list[2][41] = "Love Kome - We Love Rice Nikisaku";
#list[2][42] = "Love Live! Sunshine!! 2";
#list[2][43] = "Mahou Tsukai no Yome";
list[2][44] = "Netojuu no Susume";
list[2][45] = "Omiai Aite wa Oshiego, Tsuyoki na, Mondaiji.";
list[2][46] = "Osake wa Fuufu ni Natte kara";
list[2][47] = "Hoozuki no Reitetsu 2";
#list[2][48] = "Ou-sama Game The Animation";
list[2][49] = "RoboMasters the Animated Series";
list[2][50] = "3-gatsu no Lion 2";
list[2][51] = "Sengoku Night Blood";
list[2][52] = "Shokugeki no Souma - San no Sara";
list[2][53] = "Shoujo Shuumatsu Ryokou";
list[2][54] = "Shoujo Shuumatsu Ryokou Special";
list[2][55] = "Taishou Mebiusline - Chicchai-san";
list[2][56] = "The Idolmaster SideM";
list[2][57] = "Time Bokan - Gyakushuu no San-Okunin";
list[2][58] = "TsukiPro The Animation";
list[2][59] = "Itsudatte Bokura no Koi wa 10 Centi Datta";

list[3][0] = "2018-1";
list[3][1] = "Idolish Seven";
list[3][2] = "Sora Yori mo Tooi Basho";
list[3][3] = "25-sai no Joshikousei";
list[3][4] = "Basilisk£º Ouka Ninpouchou";
list[3][5] = "Citrus";
list[3][6] = "Gakuen Babysitters";
list[3][7] = "Grancrest Senki";
list[3][8] = "Itou Junji£º Collection";
list[3][9] = "Jian Wangchao";
list[3][10] = "Karakai Jouzu no Takagi-san";
list[3][11] = "Kokkoku";
list[3][12] = "Mitsuboshi Colors";
list[3][13] = "Nanatsu no Taizai£º Imashime no Fukkatsu";
list[3][14] = "Pochitto Hatsumei£º Pikachin-Kit";
list[3][15] = "Ramen Daisuki Koizumi-san";
list[3][16] = "Ryuuou no Oshigoto!";
list[3][17] = "Sanrio Danshi";
list[3][18] = "Shinkansen Henkei Robo Shinkalion The Animation";
list[3][19] = "Slow Start";
list[3][20] = "Toji no Miko";
list[3][21] = "Yowamushi Pedal£º Glory Line";
list[3][22] = "Yuru Camp¡â ";
list[3][23] = "Zoku Touken Ranbu£º Hanamaru";
list[3][24] = "gdMen(gdgd men¡¯s party)";

def makeDir(nm):
    check = True
    for f in os.listdir("./"):

        if f == nm:
            check = False
 
    return check

def getUpperNm(fNm):
    for season in list:
        for title in season:
            if(title == fNm):   
                return season[0]
    return "etc"
    
def mainRun():
    print("mainRun");
    
    pattern = re.compile(" - \d\d.*")
    for f in files:
        fNm = f
        fNm = fNm.replace("[Leopard-Raws]", "")
        #fNm = fNm.replace("[Ohys-Raws]", "")
        fNm = fNm.replace(pattern.search(fNm).group(0), "")
        fNm = fNm.replace(".", "")
        fNm = fNm.strip()
        upperNm = getUpperNm(fNm)
        
        if(makeDir(upperNm)):
            os.mkdir(upperNm)
        os.chdir(upperNm)
        
        if( makeDir(fNm) ):
            os.mkdir(fNm)
        os.chdir("../")   
        shutil.move(f, "./"+upperNm + "/" + fNm)

files = glob.glob("*.mp4")
mainRun()
 
files = glob.glob("*.smi")
mainRun()