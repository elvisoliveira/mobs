import bs4
import csv
import time
from bs4 import BeautifulSoup
from urllib import request

useragent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/70.0.3538.77 Safari/537.36'}

worldmaps = ["alb2trea", "alberta", "alde_gld", "aldebaran", "ama_fild01", "amatsu", "aru_gld", "ayo_fild01",
             "ayo_fild02", "ayothaya", "beach_dun", "beach_dun2", "beach_dun3", "bif_fild01", "bif_fild02",
             "bra_fild01", "brasilis", "cmd_fild01", "cmd_fild02", "cmd_fild03", "cmd_fild04", "cmd_fild05",
             "cmd_fild06", "cmd_fild07", "cmd_fild08", "cmd_fild09", "comodo", "dew_fild01", "dewata",
             "dic_dun01", "dic_fild01", "dic_fild02", "dicastes01", "dicastes02", "ecl_fild01", "eclage",
             "ein_fild01", "ein_fild02", "ein_fild03", "ein_fild04", "ein_fild05", "ein_fild06", "ein_fild07",
             "ein_fild08", "ein_fild09", "ein_fild10", "einbech", "einbroch", "gef_fild00", "gef_fild01",
             "gef_fild02", "gef_fild03", "gef_fild04", "gef_fild05", "gef_fild06", "gef_fild07", "gef_fild08",
             "gef_fild09", "gef_fild10", "gef_fild11", "gef_fild12", "gef_fild13", "gef_fild14", "geffen",
             "glast_01", "gon_fild01", "gonryun", "harboro1", "hu_fild01", "hu_fild02", "hu_fild03", "hu_fild04",
             "hu_fild05", "hu_fild06", "hu_fild07", "hugel", "izlu2dun", "izlude", "jawaii", "lasa_dun01",
             "lasa_dun02", "lasa_dun03", "lasa_fild01", "lasa_fild02", "lasagna", "lhz_fild01", "lhz_fild02",
             "lhz_fild03", "lighthalzen", "lou_fild01", "louyang", "ma_fild01", "ma_fild02", "malangdo", "malaya",
             "man_fild01", "man_fild02", "man_fild03", "manuk", "mid_camp", "mjolnir_01", "mjolnir_02", "mjolnir_03",
             "mjolnir_04", "mjolnir_05", "mjolnir_06", "mjolnir_07", "mjolnir_08", "mjolnir_09", "mjolnir_10",
             "mjolnir_11", "mjolnir_12", "moc_fild01", "moc_fild02", "moc_fild03", "moc_fild07", "moc_fild11",
             "moc_fild12", "moc_fild13", "moc_fild16", "moc_fild17", "moc_fild18", "moc_fild19", "moc_fild20",
             "moc_fild22b", "moc_ruins", "mora", "morocc", "moscovia", "nameless_n", "nif_fild01", "nif_fild02",
             "niflheim", "odin_tem01", "odin_tem02", "odin_tem03", "pay_arche", "pay_fild01", "pay_fild02",
             "pay_fild03", "pay_fild04", "pay_fild05", "pay_fild06", "pay_fild07", "pay_fild08", "pay_fild09",
             "pay_fild10", "pay_fild11", "pay_gld", "payon", "prontera", "prt_fild00", "prt_fild01", "prt_fild02",
             "prt_fild03", "prt_fild04", "prt_fild05", "prt_fild06", "prt_fild07", "prt_fild08", "prt_fild09",
             "prt_fild10", "prt_fild11", "prt_monk", "ra_fild01", "ra_fild02", "ra_fild03", "ra_fild04", "ra_fild05",
             "ra_fild06", "ra_fild07", "ra_fild08", "ra_fild09", "ra_fild10", "ra_fild11", "ra_fild12", "ra_fild13",
             "ra_temple", "rachel", "rockmi1", "rockrdg1", "rockrdg2", "sch_gld", "spl_fild01", "spl_fild02",
             "spl_fild03", "splendide", "tur_dun01", "um_dun01", "um_dun02", "um_fild01", "um_fild02", "um_fild03",
             "um_fild04", "umbala", "ve_fild01", "ve_fild02", "ve_fild03", "ve_fild04", "ve_fild05", "ve_fild07",
             "veins", "xmas", "xmas_fild01", "yggdrasil01", "yuno", "yuno_fild01", "yuno_fild02", "yuno_fild03",
             "yuno_fild04", "yuno_fild05", "yuno_fild06", "yuno_fild07", "yuno_fild08", "yuno_fild09", "yuno_fild10",
             "yuno_fild11", "yuno_fild12", "abyss_01", "abyss_02", "abyss_03", "ama_dun01", "ama_dun02", "ama_dun03",
             "anthell01", "anthell02", "ayo_dun01", "ayo_dun02", "ma_dun01", "beach_dun", "beach_dun2", "beach_dun3",
             "ecl_tdun01", "ecl_tdun02", "ecl_tdun03", "ecl_tdun04", "lhz_dun01", "lhz_dun02", "lhz_dun03", "lhz_dun04",
             "que_lhz", "lhz_dun_n", "bossnia_01", "bossnia_02", "bossnia_03", "bossnia_04", "bra_dun01", "bra_dun02",
             "izlu2dun", "iz_dun00", "iz_dun01", "iz_dun02", "iz_dun03", "iz_dun04", "iz_dun05", "c_tower1", "c_tower2",
             "c_tower3", "c_tower4", "alde_dun01", "alde_dun02", "alde_dun03", "alde_dun04", "c_tower2_", "c_tower3_",
             "mjo_dun01", "mjo_dun02", "mjo_dun03", "dew_dun01", "dew_dun02", "lasa_dun01", "lasa_dun02", "lasa_dun03",
             "lasa_dun_q", "ein_dun01", "ein_dun02", "gef_dun00", "gef_dun01", "gef_dun02", "gef_dun03", "gefenia01",
             "gefenia02", "gefenia03", "gefenia04", "glast_01", "gl_church", "gl_chyard", "gl_cas01", "gl_cas02",
             "gl_prison", "gl_prison1", "gl_knt01", "gl_knt02", "gl_in01", "gl_step", "gl_sew01", "gl_sew02",
             "gl_sew03", "gl_sew04", "gl_dun01", "gl_dun02", "gl_cas02_", "gl_chyard_", "gon_dun01", "gon_dun02",
             "gon_dun03", "gld_dun02", "gld_dun02_2", "gld2_ald", "gld_dun04", "gld_dun04_2", "gld2_gef", "gld_dun01",
             "gld_dun01_2", "gld2_pay", "gld_dun03", "gld_dun03_2", "gld2_prt", "schg_dun01", "arug_dun01", "teg_dun01",
             "teg_dun02", "prt_maze01", "prt_maze02", "prt_maze03", "ice_dun01", "ice_dun02", "ice_dun03", "ice_dun04",
             "gef_d01_i", "ice_d03_i", "pay_d03_i", "tur_d03_i", "tur_d04_i", "juperos_01", "juperos_02", "jupe_core",
             "kh_dun01", "kh_dun02", "lou_dun01", "lou_dun02", "lou_dun03", "mag_dun01", "mag_dun02", "mal_dun01",
             "mosk_dun01", "mosk_dun02", "mosk_dun03", "nameless_i", "nameless_n", "nameless_in", "abbey01", "abbey02",
             "abbey03", "nyd_dun01", "nyd_dun02", "odin_tem01", "odin_tem02", "odin_tem03", "orcsdun01", "orcsdun02",
             "pay_dun00", "pay_dun01", "pay_dun02", "pay_dun03", "pay_dun04", "prt_sewb1", "prt_sewb2", "prt_sewb3",
             "prt_sewb4", "moc_pryd01", "moc_pryd02", "moc_pryd03", "moc_pryd04", "moc_prydb1", "moc_pryd05",
             "moc_pryd06", "moc_prydn1", "moc_prydn2", "ra_temple", "ra_temin", "ra_san01", "ra_san02", "ra_san03",
             "ra_san04", "ra_san05", "rockmi1", "rockmi2", "dic_dun01", "dic_dun02", "dic_dun03", "in_sphinx1",
             "in_sphinx2", "in_sphinx3", "in_sphinx4", "in_sphinx5", "alb2trea", "treasure01", "treasure02",
             "tha_scene01", "tha_t01", "tha_t02", "tha_t03", "tha_t04", "tha_t05", "tha_t06", "tha_t07", "tha_t08",
             "tha_t09", "tha_t10", "tha_t11", "tha_t12", "thana_step", "thana_boss", "e_tower", "thor_v01", "thor_v02",
             "thor_camp", "thor_v03", "que_thor", "xmas_dun01", "xmas_dun02", "tur_dun01", "tur_dun02", "tur_dun03",
             "tur_dun04", "um_dun01", "um_dun02", "slabw01", "que_swat"]

with open('mobs_file.csv', mode='w', newline='') as mobs_file:
    employee_writer = csv.writer(mobs_file, delimiter=',')
    for worldmap in worldmaps:
        page_request = request.Request("http://ratemyserver.net/npc_shop_warp.php?map="+worldmap+"&small=1&re_mob=0",
                                       headers=useragent)
        soup = BeautifulSoup(request.urlopen(page_request).read(), "html.parser")
        aside = soup.select("table.content_box_mob")
        if len(aside) > 0:
            for mob in aside[0].findAll('tr'):
                if not mob.get('class'):
                    print(worldmap)
                    employee_writer.writerow([
                        worldmap,
                        mob.find('small').text,
                        mob.findAll('small')[1].text.split('|')[1].split(':')[1].strip(),
                        mob.findAll('td')[1].text.split(" ")[0].strip(),
                        isinstance(mob.find('small').find('span'), bs4.element.Tag)
                    ])
    time.sleep(3)
