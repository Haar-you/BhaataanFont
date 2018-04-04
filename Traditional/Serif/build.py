#!/usr/bin/env python2

import fontforge;
import psMat;

import json;
import os;

def test():
    pass;



def add_basic_consonants(font):
    f = open("consonants.json", "r");
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

        

def add_vowel_i(font):
    gl = font["bhaataan_i_raw"];
    gl.importOutlines("./glyphs/i.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    
    gl = font[0xe020];
    gl.addReference("bhaataan_i_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_i_raw");
        

def add_vowel_ii(font):
    gl = font["bhaataan_ii_raw"];
    gl.importOutlines("./glyphs/ii.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    
    gl = font[0xe023];
    gl.addReference("bhaataan_ii_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_ii_raw");

def add_vowel_au(font):
    gl = font["bhaataan_au_raw"];
    gl.importOutlines("./glyphs/au.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    
    gl = font[0xe028];
    gl.addReference("bhaataan_au_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_au_raw");



def add_vowel_u(font):
    gl = font["bhaataan_u_raw"];
    gl.importOutlines("./glyphs/u.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_u", "mark", 230, 250);
    
    gl = font[0xe021];
    gl.addReference("bhaataan_u_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_u_raw");

    
def add_vowel_aa(font):
    gl = font["bhaataan_aa_raw"];
    gl.importOutlines("./glyphs/aa.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_aa", "mark", 200, 250);
    
    gl = font[0xe022];
    gl.addReference("bhaataan_aa_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_aa_raw");

def add_vowel_uu(font):
    gl = font["bhaataan_uu_raw"];
    gl.importOutlines("./glyphs/uu.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_uu", "mark", 310, 250);
    
    gl = font[0xe024];
    gl.addReference("bhaataan_uu_raw");
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
    gl.addReference("bhaataan_e_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_e_raw");

    
def add_vowel_ai(font):
    gl = font["bhaataan_ai_raw"];
    gl.importOutlines("./glyphs/ai.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("vowel_ai", "mark", 180, 250);
    
    gl = font[0xe027];
    gl.addReference("bhaataan_ai_raw");
    gl.addReference("dotted_circle");
    gl.addPosSub("dottedcircled_to_raw-1", "bhaataan_ai_raw");

def add_vowel_no(font):
    gl = font["bhaataan_no_vowel_raw"];
    gl.importOutlines("./glyphs/novowel.svg");
    gl.left_side_bearing = 0;
    gl.right_side_bearing = 0;
    gl.width = 0;
    gl.addAnchorPoint("no_vowel", "mark", 130, 250);
    
    gl = font[0xe029];
    gl.addReference("bhaataan_no_vowel_raw");
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
    gl.width = 500;

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

    #0xe02e bhaataan_quotation_question
    font.createChar(0xe02e, "bhaataan_quotation_question");
    gl = font[0xe02e];
    gl.importOutlines("./glyphs/quotation_question.svg");
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;    
    
def add_anchorclasses(font):
    font.addLookup("mark", "gpos_mark2base", (), (("mark", (("dflt", ("dflt")),)),));
    font.addLookupSubtable("mark", "mark_subtable-1");
    font.addAnchorClass("mark_subtable-1", "vowel_u");
    font.addAnchorClass("mark_subtable-1", "vowel_aa");
    font.addAnchorClass("mark_subtable-1", "vowel_uu");
    font.addAnchorClass("mark_subtable-1", "vowel_e");
    font.addAnchorClass("mark_subtable-1", "vowel_ai");
    font.addAnchorClass("mark_subtable-1", "no_vowel");

def add_substitution(font):
    font.addLookup("dottedcircled_to_raw", "gsub_single", (), (("", (("dflt", ("dflt")),)),));
    font.addLookupSubtable("dottedcircled_to_raw", "dottedcircled_to_raw-1");

    font.addLookup("C_o_to_Co", "gsub_ligature", (), (("ccmp", (("dflt", ("dflt")),)),));
    font.addLookupSubtable("C_o_to_Co", "C_o_to_Co-1");

    
def add_contextual(font):
    consonants = " ".join(map(lambda c: "bhaataan_%s"%c ,["a", "ta", "ka", "xa", "sa", "na", "ma", "da", "ga", "pa", "ba", "ha", "ca", "za", "la", "ra", "ja", "ya", "wa", "dha", "kha", "gha", "pha", "bha", "tra", "dra", "nra", "lra", "sra", "cra"]));
    vowels = " ".join(map(lambda c: "bhaataan_%s"%c, ["i", "u", "aa", "ii", "uu", "e", "o", "ai", "au", "no_vowel"]));
    
    font.addLookup("contextualSub1", "gsub_contextchain", (), (("calt", (("dflt", ("dflt")),)),));
    font.addContextualSubtable("contextualSub1", "contextualSub1-1", "coverage",
                               "[%s] | [%s]@<dottedcircled_to_raw> |" % (consonants, vowels));


def add_kerning(font):
    
    consonants = map(lambda c: "bhaataan_%s"%c ,["a", "ta", "ka", "xa", "sa", "na", "ma", "da", "ga", "pa", "ba", "ha", "ca", "za", "la", "ra", "ja", "ya", "wa", "dha", "kha", "gha", "pha", "bha", "tra", "dra", "nra", "lra", "sra", "cra"]);
    consonants_with_o = map(lambda c: "%s_with_o"%c, consonants);

    font.addLookup("kerning1", "gpos_pair", (), (("kern", (("dflt", ("dflt")),)),));
    font.addKerningClass("kerning1", "kerning1-1",
                         [consonants + consonants_with_o + ["bhaataan_i_raw", "bhaataan_ii_raw", "bhaataan_au_raw"]],
                         [consonants + consonants_with_o, ["bhaataan_i_raw"], ["bhaataan_ii_raw"], ["bhaataan_au_raw"]],
                         [
                             -100,
                             -260,
                             -350,
                             -516
                         ]
    );


def add_with_o_consonants(font):
    consonants = map(lambda c: "bhaataan_%s"%c ,["a", "ta", "ka", "xa", "sa", "na", "ma", "da", "ga", "pa", "ba", "ha", "ca", "za", "la", "ra", "ja", "ya", "wa", "dha", "kha", "gha", "pha", "bha", "tra", "dra", "nra", "lra", "sra", "cra"]);

    for consonant in consonants:
        name = "%s_with_o" % consonant
        font.createChar(-1, name);
        gl = font[name];
        gl.addReference("bhaataan_o_raw");
        gl.addReference(consonant, psMat.translate(260,0));

        gl.left_side_bearing = 0;
        gl.right_side_bearing = 0;

        gl.addPosSub("C_o_to_Co-1", (consonant, "bhaataan_o_raw"));
        

    
    
    
def main():
    font = fontforge.font();
    font.encoding = "UnicodeBmp";
    font.familyname = "BhaataanSerif";
    font.fontname = "BhaataanSerif";
    font.fullname = "BhaataanSerif";

    font.ascent = 1000;
    font.descent = 0;

    add_anchorclasses(font);
    add_substitution(font);

    add_punctuations(font);
    add_basic_consonants(font);
    add_vowels(font);
    add_with_o_consonants(font);
    
    
    add_kerning(font);
    add_contextual(font);
    

    font.save("BhaataanSerif");
    font.generate("BhaataanSerif.ttf");
    font.generate("BhaataanSerif.woff");


    
main();

#test();
