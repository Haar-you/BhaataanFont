#!/usr/bin/env python2

import fontforge;
import psMat;

import json;
import os;


bht_consonants = ["a", "ta", "ka", "xa", "sa", "na", "ma", "da", "ga", "pa", "ba", "ha", "ca", "za", "la", "ra", "ja", "ya", "wa", "dha", "kha", "gha", "pha", "bha", "tra", "dra", "nra", "lra", "sra", "cra"];
bht_vowels =["i", "u", "aa", "ii", "uu", "e", "o", "ai", "au"];



def add_basic_consonants(font):
    f = open("consonants_.json", "r");
    data = json.load(f);

    for datum in data:
        cdpnt = int(datum.get("cdpnt", "-1"), 16);
        chrnm = str(datum.get("chrnm", ""));
        filename = datum.get("file", "");
        bearing = (0,0);
        anchors = datum.get("anchors", []);


        font.createChar(cdpnt, chrnm);
        if cdpnt != -1:
            gl = font[cdpnt];
        else:
            gl = font[chrnm];

        if filename != "":
            if os.path.exists(filename):
                gl.importOutlines(filename);
        
        gl.left_side_bearing = bearing[0];
        gl.right_side_bearing = bearing[1];

        for anchor in anchors:
            gl.addAnchorPoint(anchor["name"], "base", anchor["x"], anchor["y"]);

        gl.addAnchorPoint("vowel_aq", "base", gl.width/2, 250);

        

def add_vowel_i(font):
    gl = font["bhaataan_i_raw"];
    gl.importOutlines("./glyphs/i.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.addAnchorPoint("no_vowel", "base", 0, 250);
    
    gl = font[0xe020];
    gl.addReference("bhaataan_i_raw", psMat.translate(450,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_i_raw");
        

def add_vowel_ii(font):
    gl = font["bhaataan_ii_raw"];
    gl.importOutlines("./glyphs/ii.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.addAnchorPoint("no_vowel", "base", 110, 250);
    
    gl = font[0xe023];
    gl.addReference("bhaataan_ii_raw", psMat.translate(330,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_ii_raw");

def add_vowel_au(font):
    gl = font["bhaataan_au_raw"];
    gl.importOutlines("./glyphs/au.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.addAnchorPoint("no_vowel", "base", 290, 250);
    
    gl = font[0xe028];
    gl.addReference("bhaataan_au_raw", psMat.translate(200,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_au_raw");



def add_vowel_u(font):
    gl = font["bhaataan_u_raw"];
    gl.importOutlines("./glyphs/u.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_u", "mark", 158.5, 250);

    gl = font["bhaataan_uq_raw"];
    gl.addReference("bhaataan_u_raw", psMat.translate(100, 0));
    gl.addReference("bhaataan_no_vowel_raw");
    gl.addAnchorPoint("vowel_u", "mark", 258.5, 250);
    gl.addPosSub("VQ_liga-1", ("bhaataan_u_raw", "bhaataan_no_vowel_raw"));
  
    gl = font[0xe021];
    gl.addReference("bhaataan_u_raw", psMat.translate(400,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_u_raw");

    
def add_vowel_aa(font):
    gl = font["bhaataan_aa_raw"];
    gl.importOutlines("./glyphs/aa.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_aa", "mark", 160, 250);

    gl = font["bhaataan_aaq_raw"];
    gl.addReference("bhaataan_aa_raw", psMat.translate(100, 0));
    gl.addReference("bhaataan_no_vowel_raw");
    gl.addAnchorPoint("vowel_aa", "mark", 260, 250);
    gl.addPosSub("VQ_liga-1", ("bhaataan_aa_raw", "bhaataan_no_vowel_raw"));
    
    gl = font[0xe022];
    gl.addReference("bhaataan_aa_raw", psMat.translate(400,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_aa_raw");

def add_vowel_uu(font):
    gl = font["bhaataan_uu_raw"];
    gl.importOutlines("./glyphs/uu.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_uu", "mark", 135, 250);

    gl = font["bhaataan_uuq_raw"];
    gl.addReference("bhaataan_uu_raw", psMat.translate(100, 0));
    gl.addReference("bhaataan_no_vowel_raw");
    gl.addAnchorPoint("vowel_uu", "mark", 235, 250);
    gl.addPosSub("VQ_liga-1", ("bhaataan_uu_raw", "bhaataan_no_vowel_raw"));
    
    gl = font[0xe024];
    gl.addReference("bhaataan_uu_raw", psMat.translate(400,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_uu_raw");

def add_vowel_e(font):
    gl = font["bhaataan_e_raw"];
    gl.importOutlines("./glyphs/e.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_e", "mark", 0, 750);
    
    gl = font[0xe025];
    gl.addReference("bhaataan_e_raw", psMat.translate(400,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_e_raw");

    
def add_vowel_ai(font):
    gl = font["bhaataan_ai_raw"];
    gl.importOutlines("./glyphs/ai.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_ai", "mark", 135, 250);

    gl = font["bhaataan_aiq_raw"];
    gl.addReference("bhaataan_ai_raw", psMat.translate(100, 0));
    gl.addReference("bhaataan_no_vowel_raw");
    gl.addAnchorPoint("vowel_ai", "mark", 235, 250);
    gl.addPosSub("VQ_liga-1", ("bhaataan_ai_raw", "bhaataan_no_vowel_raw"));
    
    gl = font[0xe027];
    gl.addReference("bhaataan_ai_raw", psMat.translate(400,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_ai_raw");

def add_vowel_no(font):
    gl = font["bhaataan_no_vowel_raw"];
    gl.importOutlines("./glyphs/novowel.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("no_vowel", "mark", 30, 250);
    
    gl = font[0xe029];
    gl.addReference("bhaataan_no_vowel_raw", psMat.translate(400,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_no_vowel_raw");

def add_vowel_o(font):
    gl = font["bhaataan_o_raw"];
    gl.importOutlines("./glyphs/o.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;

    gl = font[0xe026];
    gl.addReference("bhaataan_o_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_o_raw");

def add_vowel_aq(font):
    gl = font["bhaataan_aq_raw"];
    gl.importOutlines("./glyphs/aq.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_aq", "mark", 220, 250);

    gl = font[0xe02f];
    gl.addReference("bhaataan_aq_raw", psMat.translate(400,0));
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_aq_raw");


def add_vowels(font):

    font.createChar(0xe020, "bhaataan_i");
    font.createChar(0xe021, "bhaataan_u");
    font.createChar(0xe022, "bhaataan_aa");
    font.createChar(0xe023, "bhaataan_ii");
    font.createChar(0xe024, "bhaataan_uu");
    font.createChar(0xe025, "bhaataan_e");
    font.createChar(0xe026, "bhaataan_o");
    font.createChar(0xe027, "bhaataan_ai");
    font.createChar(0xe028, "bhaataan_au");
    font.createChar(0xe029, "bhaataan_no_vowel");

    font.createChar(0xe02f, "bhaataan_aq");

    
    font.createChar(-1, "bhaataan_i_raw");
    font.createChar(-1, "bhaataan_u_raw");
    font.createChar(-1, "bhaataan_aa_raw");
    font.createChar(-1, "bhaataan_ii_raw");
    font.createChar(-1, "bhaataan_uu_raw");
    font.createChar(-1, "bhaataan_e_raw");
    font.createChar(-1, "bhaataan_o_raw");
    font.createChar(-1, "bhaataan_ai_raw");
    font.createChar(-1, "bhaataan_au_raw");
    font.createChar(-1, "bhaataan_no_vowel_raw");


    font.createChar(-1, "bhaataan_uq_raw");
    font.createChar(-1, "bhaataan_aaq_raw");
    font.createChar(-1, "bhaataan_uuq_raw");
    font.createChar(-1, "bhaataan_aiq_raw");
    font.createChar(-1, "bhaataan_aq_raw");

    add_vowel_aq(font);

    add_vowel_i(font);
    add_vowel_u(font);

    add_vowel_aa(font);
    add_vowel_ii(font);
    add_vowel_uu(font);

    add_vowel_e(font);
    add_vowel_o(font);

    add_vowel_ai(font);
    add_vowel_au(font);

    add_vowel_no(font);
    
    
    

def add_punctuations(font):
    #0x25cc dotted_circle
    font.createChar(0x25cc, "dotted_circle");
    gl = font[0x25cc];
    gl.importOutlines("./glyphs/dottedcircle.svg");
        
    #0x0020 space
    font.createChar(0x0020, "space");
    gl = font[0x0020];
    gl.width = 400;

    #0xe02a bhaataan_period
    font.createChar(0xe02a, "bhaataan_period");
    gl = font[0xe02a];
    gl.importOutlines("./glyphs/period.svg");
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;

    #0xe02b bhaataan_comma
    font.createChar(0xe02b, "bhaataan_comma");
    gl = font[0xe02b];
    gl.importOutlines("./glyphs/comma.svg");
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;

    #0xe02c bhaataan_quotation
    font.createChar(0xe02c, "bhaataan_quotation");
    gl = font[0xe02c];
    gl.importOutlines("./glyphs/quotation.svg");
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;

    #0xe02d bhaataan_question
    font.createChar(0xe02d, "bhaataan_question");
    gl = font[0xe02d];
    gl.importOutlines("./glyphs/question.svg");
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;

    #0xe02e bhaataan_question_quotation
    font.createChar(0xe02e, "bhaataan_question_quotation");
    gl = font[0xe02e];
    gl.importOutlines("./glyphs/question_quotation.svg");
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;
    
def add_anchorclasses(font):
    font.addLookup("mark1", "gpos_mark2base", (), (("mark", (("dflt", ("dflt")),)),));
    font.addLookupSubtable("mark1", "mark1-1");
    font.addAnchorClass("mark1-1", "vowel_u");
    font.addAnchorClass("mark1-1", "vowel_aa");
    font.addAnchorClass("mark1-1", "vowel_uu");
    font.addAnchorClass("mark1-1", "vowel_e");
    font.addAnchorClass("mark1-1", "vowel_ai");
    font.addAnchorClass("mark1-1", "no_vowel");
    font.addAnchorClass("mark1-1", "vowel_aq");


def add_substitution(font):
    font.addLookup("dottedcircled_to_raw", "gsub_single", (), (("", (("dflt", ("dflt")),)),));
    font.addLookupSubtable("dottedcircled_to_raw", "dottedcircled_to_raw-1");

    font.addLookup("C_o_to_Co", "gsub_ligature", (), (("ccmp", (("dflt", ("dflt")),)),));
    font.addLookupSubtable("C_o_to_Co", "C_o_to_Co-1");

    font.addLookup("VQ_liga", "gsub_ligature", (), (("ccmp", (("dflt", ("dflt")),)),));
    font.addLookupSubtable("VQ_liga", "VQ_liga-1");
    
def add_contextual_chaining(font):
    consonants = " ".join(map(lambda c: "bhaataan_%s"%c, bht_consonants));
    vowels_nvmark = " ".join(map(lambda c: "bhaataan_%s"%c, bht_vowels + ["no_vowel"])); #nv = no vowel
    vowels = " ".join(map(lambda c: "bhaataan_%s"%c, bht_vowels));
    
    font.addLookup("contextualSub1", "gsub_contextchain", (), (("calt", (("dflt", ("dflt")),)),));
    font.addContextualSubtable("contextualSub1", "contextualSub1-1", "coverage",
                               "[%s] | [%s]@<dottedcircled_to_raw> |" % (consonants, vowels_nvmark + " bhaataan_aq"));

    font.addLookup("contextualSub2", "gsub_contextchain", (), (("calt", (("dflt", ("dflt")),)),));
    font.addContextualSubtable("contextualSub2", "contextualSub2-1", "coverage",
                               "[%s] | [%s]@<dottedcircled_to_raw> [%s]@<dottedcircled_to_raw> |" % (consonants, vowels, "bhaataan_no_vowel"));

    

    consonants_with_o = " ".join(map(lambda c: "bhaataan_%s_with_o"%c, bht_consonants));
    character_with_bar = " ".join([consonants, consonants_with_o, (" ".join(["bhaataan_i_raw", "bhaataan_ii_raw", "bhaataan_au_raw"]))])
    character_mark = " ".join(["bhaataan_u_raw", "bhaataan_aa_raw", "bhaataan_uu_raw", "bhaataan_e_raw", "bhaataan_ai_raw", "bhaataan_no_vowel_raw", "bhaataan_uq_raw", "bhaataan_aaq_raw", "bhaataan_uuq_raw", "bhaataan_aiq_raw", "bhaataan_aq_raw"])
    
    #font.addLookup("contextualPos1", "gpos_contextchain", (),(("calt", (("dflt", ("dflt")),)),));
    #font.addContextualSubtable("contextualPos1", "contextualPos1-1", "coverage",
    #                           "[%s] [%s] | [%s]@<singlepos1> |" % (character_with_bar, character_mark, character_with_bar));

    #font.addLookup("contextualPos2", "gpos_contextchain", (),(("calt", (("dflt", ("dflt")),)),));
    #font.addContextualSubtable("contextualPos2", "contextualPos2-1", "coverage",
    #                           "[%s] [%s] [%s] | [%s]@<singlepos1> |" % (character_with_bar, character_mark, character_mark, character_with_bar));

def add_kerning(font):
    
    consonants = map(lambda c: "bhaataan_%s"%c ,["a", "ta", "ka", "xa", "sa", "na", "ma", "da", "ga", "pa", "ba", "ha", "ca", "za", "la", "ra", "ja", "ya", "wa", "dha", "kha", "gha", "pha", "bha", "tra", "dra", "nra", "lra", "sra", "cra"]);
    consonants_with_o = map(lambda c: "%s_with_o"%c, consonants);

    font.addLookup("kerning1", "gpos_pair", (), (("kern", (("dflt", ("dflt")),)),));
    font.addKerningClass("kerning1", "kerning1-1",
                         [consonants + consonants_with_o + ["bhaataan_i_raw", "bhaataan_ii_raw", "bhaataan_au_raw"]],
                         [[], consonants + consonants_with_o, ["bhaataan_i_raw"], ["bhaataan_ii_raw"], ["bhaataan_au_raw"]],
                         [
                             0, 0, -200, -320, -400
                         ]
    );

    #font.addLookup("singlepos1", "gpos_single", (), (("", (("dflt", ("dflt")),)),));
    #font.addLookupSubtable("singlepos1", "singlepos1-1");
    #for c in consonants + consonants_with_o + ["bhaataan_i_raw", "bhaataan_ii_raw", "bhaataan_au_raw"]:
    #    gl = font[c];
    #    gl.addPosSub("singlepos1-1", 0, 0, 0, 0);
    

def add_with_o_consonants(font):
    consonants = map(lambda c: "bhaataan_%s"%c ,["a", "ta", "ka", "xa", "sa", "na", "ma", "da", "ga", "pa", "ba", "ha", "ca", "za", "la", "ra", "ja", "ya", "wa", "dha", "kha", "gha", "pha", "bha", "tra", "dra", "nra", "lra", "sra", "cra"]);

    for consonant in consonants:
        name = "%s_with_o" % consonant
        font.createChar(-1, name);
        gl = font[name];
        gl.addReference("bhaataan_o_raw");
        gl.addReference(consonant, psMat.translate(360,0));

        for anc in font[consonant].anchorPoints:
            if anc[0] == "no_vowel":
                gl.addAnchorPoint("no_vowel", "base", 360 + anc[2], 250);
                break;


        gl.left_side_bearing = 0;
        gl.right_side_bearing = 0;

        gl.addPosSub("C_o_to_Co-1", (consonant, "bhaataan_o_raw"));
        

    
    
    
def main():
    name = "Bhaataan-HighContrast-Serif"
    font = fontforge.font();
    font.encoding = "UnicodeBmp";
    font.familyname = name;
    font.fontname = name;
    font.fullname = name;

    font.ascent = 1000;
    font.descent = 0;

    add_anchorclasses(font);
    add_substitution(font);

    add_punctuations(font);
    add_basic_consonants(font);
    add_vowels(font);
    add_with_o_consonants(font);
    
    
    add_kerning(font);
    add_contextual_chaining(font);
    

    font.save(name);
    font.generate("%s.ttf" % name);
    font.generate("%s.woff" % name);


    
main();

