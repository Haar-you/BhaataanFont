#!/usr/bin/env python2
#coding: utf-8

import fontforge;
import psMat;

bhat_consonants = ["a", "ta", "ka", "xa", "sa", "na", "ma", "da", "ga", "pa", "ba", "ha", "ca", "za", "la", "ra", "ja", "ya", "wa", "dha", "kha", "gha", "pha", "bha", "tra", "dra", "nra", "lra", "cra"];
bhat_vowels = ["i", "u", "aa", "ii", "uu", "e" ,"o", "ai", "au", "novowel"];

gldir = "../Traditional/glyphs"

def create_characters(font):
    for cp in range(0x0000, 0x0080): #基本ラテン字
        font.createChar(cp);

    for cp in [0x1e0c, 0x1e0d, 0x1e36, 0x1e37, 0x1e46, 0x1e47, 0x1e62, 0x1e63, 0x1e6c, 0x1e6d, 0x00c1, 0x00cd, 0x00da, 0x00e1, 0x00ed, 0x00fa]:
        font.createChar(cp);

def create(font):    
    for cp in bhat_consonants:        
        font.createChar(-1, "bhat_%s" % cp);
        font["bhat_%s" % cp].importOutlines("%s/%s.svg" % (gldir, cp));
        font["bhat_%s" % cp].right_side_bearing = 0;
        font["bhat_%s" % cp].left_side_bearing = 0;

    for cp in bhat_vowels:
        font.createChar(-1, "bhat_%s_mark" % cp);
        font["bhat_%s_mark" % cp].importOutlines("%s/%s.svg" % (gldir, cp));
        font["bhat_%s_mark" % cp].right_side_bearing = 0;
        font["bhat_%s_mark" % cp].left_side_bearing = 0;

    bar_left = {"i": 270.06, "ii": 350.75,"au": 530.06}
    
    for cns in bhat_consonants:
        for vwl in bhat_vowels:
            if vwl == "a":
                pass;
            elif vwl == "novowel":
                font.createChar(-1, "bhat_%s" % cns[0:-1]);
                font["bhat_%s" % (cns[0:-1])].addReference("bhat_%sa" % cns[0:-1]);
                font["bhat_%s" % (cns[0:-1])].addReference("bhat_novowel_mark", psMat.translate(font["bhat_%s" % cns].width / 3, 0));
                
            elif vwl == "i" or vwl == "ii" or vwl == "au":
                font.createChar(-1, "bhat_%s%s" % (cns[0:-1], vwl));
                font["bhat_%s%s" % (cns[0:-1], vwl)].addReference("bhat_%sa" % cns[0:-1]);
                font["bhat_%s%s" % (cns[0:-1], vwl)].addReference("bhat_%s_mark" % vwl, psMat.translate(font["bhat_%s" % cns].width - bar_left[vwl], 0));

            elif vwl == "o":
                font.createChar(-1, "bhat_%s%s" % (cns[0:-1], vwl));
                font["bhat_%s%s" % (cns[0:-1], vwl)].addReference("bhat_%sa" % cns[0:-1], psMat.translate(260, 0));
                font["bhat_%s%s" % (cns[0:-1], vwl)].addReference("bhat_%s_mark" % vwl);
                
            else:
                font.createChar(-1, "bhat_%s%s" % (cns[0:-1], vwl));
                font["bhat_%s%s" % (cns[0:-1], vwl)].addReference("bhat_%sa" % cns[0:-1]);
                font["bhat_%s%s" % (cns[0:-1], vwl)].addReference("bhat_%s_mark" % vwl, psMat.translate(font["bhat_%s" % cns].width / 3, 0));

    for cp in ["t", "k", "x", "s", "n", "m", "d", "g", "p", "b", "h", "c", "z", "l", "r", "j", "y", "w"]:
        font[cp].addReference("bhat_%s" % cp);        
        font[cp.upper()].addReference("bhat_%s" % cp);

    for cp in ["a", "i", "u", "e", "o"]:
        font[cp].addReference("bhat_%s" % cp);
        font[cp.upper()].addReference("bhat_%s" % cp);


    font.addLookup("ligature1", "gsub_ligature", (), (("ccmp",(("DFLT",("dflt")), ("latn",("dflt")))),));
    font.addLookupSubtable("ligature1", "ligature1-1");

    for nm in ["ai", "au", "dh", "kh", "gh", "ph", "bh"]:
        font["bhat_%s" % nm].addPosSub("ligature1-1", (nm[0], nm[1]));
        font["bhat_%s" % nm].addPosSub("ligature1-1", (nm[0].upper(), nm[1]));
        font["bhat_%s" % nm].addPosSub("ligature1-1", (nm[0], nm[1].upper()));
        font["bhat_%s" % nm].addPosSub("ligature1-1", (nm[0].upper(), nm[1].upper()));

    for el in [("uni1E0C", "dr"), ("uni1E0D", "dr"), ("uni1E36", "lr"), ("uni1E37", "lr"), ("uni1E46", "nr"), ("uni1E47", "nr"), ("uni1E62", "cr"), ("uni1E63", "cr"), ("uni1E6C", "tr"), ("uni1E6D", "tr"), ("Aacute", "aa"), ("aacute", "aa"), ("Iacute", "ii"), ("iacute", "ii"), ("Uacute", "uu"), ("uacute", "uu")]:
        font[el[0]].addReference("bhat_%s" % el[1]);


    for cns in map(lambda x: (list(x), x),["t", "k", "x", "s", "n", "m", "d", "g", "p", "b", "h", "c", "z", "l", "r", "j", "y", "w", "dh", "kh", "gh", "ph", "bh", ]) + [(["uni1E0C"], "dr"), (["uni1E0D"], "dr"), (["uni1E36"], "lr"), (["uni1E37"], "lr"), (["uni1E46"], "nr"), (["uni1E47"], "nr"), (["uni1E62"], "cr"), (["uni1E63"], "cr"), (["uni1E6C"], "tr"), (["uni1E6D"], "tr")]:
        for vwl in map(lambda x: (list(x), x), ["a", "i", "u", "e", "o", "ai", "au"]) + [(["Aacute"], "aa"), (["aacute"], "aa"), (["Iacute"], "ii"), (["iacute"], "ii"), (["Uacute"], "uu"), (["uacute"], "uu")]:
            syl = cns[1] + vwl[1];
            lst = cns[0] + vwl[0];
            font["bhat_%s" % syl].addPosSub("ligature1-1", lst);

    all_composed = " ".join(
        reduce(lambda x, y: x+y,
            map(lambda v:
                map(lambda c: "bhat_%s%s" % (c, v), ["", "t", "k", "x", "s", "n", "m", "d", "g", "p", "b", "h", "c", "z", "l", "r", "j", "y", "w", "dh", "kh", "gh", "ph", "bh", "tr", "dr", "nr", "lr", "cr"]), ["a", "i", "u", "aa", "ii", "uu", "e", "o", "ai", "au", ""]))
        + ["a", "i", "u", "e", "o", "t", "k", "x", "s", "n", "m", "d", "g", "p", "b", "h", "c", "z", "l", "r", "j", "y", "w"]
        + map(lambda x: x.upper(), ["a", "i", "u", "e", "o", "t", "k", "x", "s", "n", "m", "d", "g", "p", "b", "h", "c", "z", "l", "r", "j", "y", "w"])
        + ["uni1E0C", "uni1E0D", "uni1E36", "uni1E37", "uni1E46", "uni1E47", "uni1E62", "uni1E63", "uni1E6C", "uni1E6D", "Aacute", "aacute", "Iacute", "iacute", "Uacute", "uacute"]
    );
    
    font.addLookup("kerning1", "gpos_pair", (), (("kern",(("dflt",("dflt")), ("latn",("dflt")))),));
    font.addKerningClass("kerning1", "kerning1-1", [all_composed], [[], all_composed], [0, -100]);

    for cp in font:
        font[cp].right_side_bearing = 0;
        font[cp].left_side_bearing = 0;

    font["space"].width = 200;

    


def main():
    font = fontforge.font();
    name = "BhataanTransliteration"

    font.fullname = name;
    font.fontname = name;
    font.familyname = name;

    font.encoding = "UnicodeBmp";

    create_characters(font);
    create(font);
    
    font.save("%s.sfd" % name);
    font.generate("%s.ttf" % name);
    font.generate("%s.woff" % name);

main();

