import xml.etree.ElementTree as ET
import pdb
import pathlib

black = "#292524"
orange = "#DB4B1A"
yellow = "#C6D431"
ybrown = "#7A6B1C"
silver = "#88898c"
white = "#FFFFEc"
peach = "#ebdba2"


female_classes = {
    "body": {
        "head_integument": None,
        "head": ["face", "vertex"],
        "mesosoma": {
            "propodeum": ["propodeum_l", "propodeum_m", "propodeum_r" ],
            "scutum": ["scutum_lr", "scutum_m"],
            "pronotum": None,
            "mesosoma_side": ["mesosoma_pr", "mesosoma_ar", "mesosoma_pl", "mesosoma_al"],
        },
        "metasoma": {
            "T1": ["T1_r", "T1_m", "T1_l" ],
            "T2": {
                "T2_a": ["T2_ar", "T2_am", "T2_al" ],
                "T2_p": ["T2_pr", "T2_pm", "T2_pl" ],
            },
            "T3": {
                "T3_a": ["T3_ar", "T3_am", "T3_al" ],
                "T3_p": ["T3_pr", "T3_pm", "T3_pl" ],
            },
            "T4": {
                "T4_a": ["T4_ar", "T4_am", "T4_al" ],
                "T4_p": ["T4_pr", "T4_pm", "T4_pl" ],
            },
            "T5": {
                "T5_a": ["T5_ar", "T5_am", "T5_al" ],
                "T5_p": ["T5_pr", "T5_pm", "T5_pl" ],
            },
            "T6": None
        },
    }
}

female_default_colors = {
    "face": yellow,
    "head_integument": black,
    "vertex": yellow,
    "pronotum": yellow,
    "mesosoma_pr": yellow, 
    "mesosoma_ar": yellow, 
    "mesosoma_pl": yellow, 
    "mesosoma_al": yellow,
    "scutum_lr": yellow,
    "scutum_m": black,
    "scutum_lr": yellow,
    "propodeum_l": yellow,
    "propodeum_m": yellow,
    "propodeum_r": yellow,
    "T1_l": yellow,
    "T1_m": yellow,
    "T1_r": yellow,
    "T2_al": yellow,
    "T2_am": yellow,
    "T2_ar": yellow,
    "T2_pl": yellow,
    "T2_pm": yellow,
    "T2_pr": yellow,
    "T3_al": yellow,
    "T3_am": yellow,
    "T3_ar": yellow,
    "T3_pl": yellow,
    "T3_pm": yellow,
    "T3_pr": yellow,
    "T4_al": yellow,
    "T4_am": yellow,
    "T4_ar": yellow,
    "T4_pm": yellow,
    "T4_pr": yellow,
    "T4_pl": yellow,
    "T5_al": yellow,
    "T5_am": yellow,
    "T5_ar": yellow,
    "T5_pm": yellow,
    "T5_pr": yellow,
    "T5_pl": yellow,
    "T6": black,
}

male_classes = {
    "body": {
        "head_integument": None,
        "head": ["face", "vertex"],
        "mesosoma": {
            "propodeum": ["propodeum_l", "propodeum_m", "propodeum_r" ],
            "scutum": ["scutum_lr", "scutum_m"],
            "pronotum": None,
            "mesosoma_side": ["mesosoma_pr", "mesosoma_ar", "mesosoma_pl", "mesosoma_al"],
        },
        "metasoma": {
            "T1": ["T1_r", "T1_m", "T1_l" ],
            "T2": {
                "T2_a": ["T2_ar", "T2_am", "T2_al" ],
                "T2_p": ["T2_pr", "T2_pm", "T2_pl" ],
            },
            "T3": {
                "T3_a": ["T3_ar", "T3_am", "T3_al" ],
                "T3_p": ["T3_pr", "T3_pm", "T3_pl" ],
            },
            "T4": {
                "T4_a": ["T4_ar", "T4_am", "T4_al" ],
                "T4_p": ["T4_pr", "T4_pm", "T4_pl" ],
            },
            "T5": {
                "T5_a": ["T5_ar", "T5_am", "T5_al" ],
                "T5_p": ["T5_pr", "T5_pm", "T5_pl" ],
            },
            "T6": {
                "T6_a": ["T6_ar", "T6_am", "T6_al" ],
                "T6_p": ["T6_pr", "T6_pm", "T6_pl" ],
            },
            "T7": None
        },
    }
}

male_default_colors = {
    "face": yellow,
    "head_integument": black,
    "vertex": yellow,
    "pronotum": yellow,
    "mesosoma_pr": yellow, 
    "mesosoma_ar": yellow, 
    "mesosoma_pl": yellow, 
    "mesosoma_al": yellow,
    "scutum_lr": yellow,
    "scutum_m": black,
    "scutum_lr": yellow,
    "propodeum_l": yellow,
    "propodeum_m": yellow,
    "propodeum_r": yellow,
    "T1_l": yellow,
    "T1_m": yellow,
    "T1_r": yellow,
    "T2_al": yellow,
    "T2_am": yellow,
    "T2_ar": yellow,
    "T2_pl": yellow,
    "T2_pm": yellow,
    "T2_pr": yellow,
    "T3_al": yellow,
    "T3_am": yellow,
    "T3_ar": yellow,
    "T3_pl": yellow,
    "T3_pm": yellow,
    "T3_pr": yellow,
    "T4_al": yellow,
    "T4_am": yellow,
    "T4_ar": yellow,
    "T4_pm": yellow,
    "T4_pr": yellow,
    "T4_pl": yellow,
    "T5_al": yellow,
    "T5_am": yellow,
    "T5_ar": yellow,
    "T5_pm": yellow,
    "T5_pr": yellow,
    "T5_pl": yellow,
    "T6_al": yellow,
    "T6_am": yellow,
    "T6_ar": yellow,
    "T6_pm": yellow,
    "T6_pr": yellow,
    "T6_pl": yellow,
    "T7": black,
}

patterns = {
    "appositus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "fervidus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "centralis": {
        "queen": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "metasoma": yellow,
                "T3": orange,
                "T4": orange,
                "T5": black,
                "T6": black,
            },
        ],
        "worker": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "metasoma": yellow,
                "T3": orange,
                "T4": orange,
                "T5": black,
                "T6": black,
            },
            {
                "head": yellow,
                "vertex": ybrown,
                "mesosoma": yellow,
                "scutum": black,
                "metasoma": yellow,
                "T3": orange,
                "T4": orange,
                "T5": black,
                "T6": black,
            },
        ],
        "male": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "metasoma": orange,
                "T1": yellow,
                "T2": yellow,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "scutum_m": black,
                "metasoma": orange,
                "T1": yellow,
                "T2": yellow,
                "T6_p": black,
                "T7": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "metasoma": orange,
                "T1": yellow,
                "T2": yellow,
                "T3": orange,
                "T4": orange,
                "T5": black,
                "T6": black,
                "T7": black,
            },
        ],
    },
    "flavidus": {
    },
    "flavifrons": {
        "queen": [
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum_m": black,
                "metasoma": yellow,
                "T3": orange,
                "T4": orange,
                "T5": black,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum_m": black,
                "metasoma": yellow,
                "T1_m": black,
                "T2_am": black,
                "T3": orange,
                "T4": orange,
                "T5_a": black,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum_m": black,
                "metasoma": yellow,
                "T1_m": black,
                "T2_am": black,
                "T3": orange,
                "T3_ar": black,
                "T3_al": black,
                "T4": black,
                "T5": black,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum": black,
                "metasoma": black,
                "T1_l": yellow,
                "T1_r": yellow,
                "T2_ar": yellow,
                "T2_al": yellow,
                "T2_p": yellow,
            },
            {
                "head": yellow,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum": black,
                "metasoma": black,
                "T1": yellow,
                "T2": yellow,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "metasoma": black,
                "T1_l": yellow,
                "T1_r": yellow,
                "T2": yellow,
                "T2_am": black,
            },
        ],
        "worker": [
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum_m": black,
                "metasoma": yellow,
                "T3": orange,
                "T4": orange,
                "T5": black,
                "T6": black,
            },
            {
                "head": ybrown,
                "face": yellow,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum_m": black,
                "metasoma": yellow,
                "T3": orange,
                "T4": orange,
                "T5_a": black,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum_m": black,
                "metasoma": yellow,
                "T1_m": black,
                "T2_am": black,
                "T3": orange,
                "T3_ar": black,
                "T3_al": black,
                "T4": black,
                "T5": black,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum_m": black,
                "metasoma": black,
                "T1_l": yellow,
                "T1_r": yellow,
                "T2_ar": yellow,
                "T2_al": yellow,
                "T2_p": yellow,
            },
            {
                "head": yellow,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum": black,
                "metasoma": black,
                "T1": yellow,
                "T2": yellow,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "metasoma": black,
                "T1_l": yellow,
                "T1_m": ybrown,
                "T1_r": yellow,
                "T2": yellow,
                "T2_am": black,
            },
        ],
        "male": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "propodeum_m": ybrown,
                "metasoma": black,
                "T1": yellow,
                "T2": yellow,
                "T3": orange,
                "T4": orange,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": black,
                "T1": yellow,
                "T2": yellow,
                "T3": orange,
                "T4": orange,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "pronotum": ybrown,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": black,
                "T1": yellow,
                "T2": yellow,
                "T3": orange,
                "T4": orange,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T5_a": black,
                "T5_pm": black,
                "T6_a": black,
                "T6_pm": black,
                "T7": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "propodeum_m": ybrown,
                "metasoma": yellow,
                "T3_a": ybrown,
                "T4_a": ybrown,
                "T5_a": black,
                "T5_pm": black,
                "T6_a": black,
                "T6_pm": black,
                "T7": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "propodeum_m": ybrown,
                "metasoma": yellow,
                "T3_a": black,
                "T4_a": black,
                "T5_a": black,
                "T5_pm": black,
                "T6_a": black,
                "T6_p": black,
                "T7": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T3_a": black,
                "T3_pm": ybrown,
                "T4": black,
                "T5": black,
                "T6": black,
                "T7": black,
            },

        ],
    },
    "frigidus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "griseocolis": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "huntii": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "impatiens": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "insularis": {
    },
    "kirbiellus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "melanopygus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "mixtus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "morrisoni": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "nevadensis": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "occidentalis": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "rufocinctus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "sitkensis": {
        "queen": [
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "metasoma": yellow,
                "T3": black,
                "T4_a": black,
                "T4_p": peach,
                "T5": peach,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "propodeum": black,
                "metasoma": yellow,
                "T3": black,
                "T4_a": black,
                "T4_p": peach,
                "T5": peach,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum": black,
                "propodeum": black,
                "metasoma": yellow,
                "T2_pm": black,
                "T3": black,
                "T4_a": black,
                "T4_p": peach,
                "T5": peach,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum": black,
                "propodeum": black,
                "metasoma": yellow,
                "T1_m": ybrown,
                "T2_a": ybrown,
                "T2_pm": black,
                "T3": black,
                "T4_a": black,
                "T4_p": peach,
                "T5": peach,
                "T6": black,
            },
        ],
        "worker": [
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T3_a": black,
                "T3_p": ybrown,
                "T4": black,
                "T4_pm": peach,
                "T5": peach,
                "T6": black,
            },
            {
                "head": ybrown,
                "mesosoma": ybrown,
                "mesosoma_side": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T3": black,
                "T4": black,
                "T4_pm": peach,
                "T5": peach,
                "T6": black,
            },
        ],
        "male": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "propodeum_m": ybrown,
                "metasoma": yellow,
                "T4_a": ybrown,
                "T5_a": black,
                "T5_p": peach,
                "T6": peach,
                "T7": peach,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "propodeum_m": ybrown,
                "metasoma": yellow,
                "T3_a": black,
                "T4_a": black,
                "T5_a": black,
                "T5_p": peach,
                "T6": peach,
                "T7": peach,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "propodeum_m": ybrown,
                "metasoma": yellow,
                "T3_a": black,
                "T4": black,
                "T5_a": black,
                "T5_p": peach,
                "T6": peach,
                "T7": peach,
            },
        ],
    },
    "suckleyi": {
    },
    "sylvicola": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "vagans": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "vancouverensis": {
        "queen": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "T1": yellow,
                "T2": orange,
                "T2_am": black,
                "T3": orange,
                "T4": yellow,
                "T5": black,
                "T5_pl": yellow,
                "T5_pr": yellow,
            },
            {
                "head": silver,
                "mesosoma": black,
                "pronotum": silver,
                "mesosoma_ar": white,
                "mesosoma_al": white,
                "mesosoma_pr": silver,
                "mesosoma_pl": silver,
                "propodeum_r": white,
                "propodeum_l": white,
                "T1": yellow,
                "T2": orange,
                "T2_am": black,
                "T3": orange,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": silver,
                "mesosoma": black,
                "pronotum": silver,
                "mesosoma_ar": white,
                "mesosoma_al": white,
                "mesosoma_pr": silver,
                "mesosoma_pl": silver,
                "propodeum_r": white,
                "propodeum_l": white,
                "T1": yellow,
                "T2": orange,
                "T2_a": black,
                "T2_pm": black,
                "T3": orange,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": white,
                "mesosoma": black,
                "pronotum": silver,
                "mesosoma_ar": white,
                "mesosoma_al": white,
                "mesosoma_pr": black,
                "mesosoma_pl": black,
                "propodeum_r": white,
                "propodeum_l": white,
                "T1": yellow,
                "T2": orange,
                "T2_a": black,
                "T2_pm": black,
                "T3": orange,
                "T3_a": black,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": white,
                "mesosoma": black,
                "pronotum": silver,
                "mesosoma_ar": white,
                "mesosoma_al": white,
                "propodeum_r": white,
                "propodeum_l": white,
                "T1": yellow,
                "T2": black,
                "T3": black,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": ybrown,
                "mesosoma_ar": yellow,
                "mesosoma_al": yellow,
                "propodeum_r": yellow,
                "propodeum_l": yellow,
                "T1": yellow,
                "T2": black,
                "T3": black,
                "T4": yellow,
                "T5": black,
            },
        ],
        "worker": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "T1": yellow,
                "T2": orange,
                "T2_am": black,
                "T3": orange,
                "T4": yellow,
                "T5": black,
                "T5_pr": yellow,
                "T5_pl": yellow,
            },
            {
                "head": silver,
                "mesosoma": black,
                "pronotum": silver,
                "mesosoma_al": white,
                "mesosoma_ar": white,
                "propodeum_l": white,
                "propodeum_r": white,
                "propodeum_m": black,
                "T1": white,
                "T2": orange,
                "T2_am": black,
                "T3": orange,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": silver,
                "mesosoma": black,
                "pronotum": silver,
                "mesosoma_al": white,
                "mesosoma_ar": white,
                "propodeum_l": white,
                "propodeum_r": white,
                "propodeum_m": black,
                "T1": white,
                "T2": black,
                "T2_pl": orange,
                "T2_pr": orange,
                "T3": orange,
                "T3_am": black,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": silver,
                "mesosoma": black,
                "pronotum": silver,
                "mesosoma_al": white,
                "mesosoma_ar": white,
                "propodeum_l": yellow,
                "propodeum_r": yellow,
                "propodeum_m": black,
                "T1": yellow,
                "T2": black,
                "T2_pl": orange,
                "T2_pr": orange,
                "T3": black,
                "T3_pr": orange,
                "T3_pl": orange,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": ybrown,
                "mesosoma": black,
                "pronotum": ybrown,
                "mesosoma_al": yellow,
                "mesosoma_ar": yellow,
                "propodeum_l": yellow,
                "propodeum_r": yellow,
                "propodeum_m": black,
                "T1": yellow,
                "T2": black,
                "T3": black,
                "T3_pr": orange,
                "T3_pl": orange,
                "T4": yellow,
                "T5": black,
            },
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": ybrown,
                "mesosoma_al": yellow,
                "mesosoma_ar": yellow,
                "propodeum_l": yellow,
                "propodeum_r": yellow,
                "T1": yellow,
                "T2": black,
                "T3": black,
                "T5": black,
            },
        ],
        "male": [
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T2_al": orange,
                "T2_ar": orange,
                "T2_pl": orange,
                "T2_pr": orange,
                "T3": orange,
                "T5_a": black,
                "T5_pm": black,
                "T6": black,
                "T7": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T2_al": black,
                "T2_ar": black,
                "T2_p": orange,
                "T2_pm": black,
                "T3": orange,
                "T5_a": ybrown,
                "T6": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": ybrown,
                "propodeum_m": ybrown,
                "metasoma": yellow,
                "T2_al": black,
                "T2_ar": black,
                "T2_pl": black,
                "T2_pr": black,
                "T3": black,
                "T5_al": ybrown,
                "T5_am": black,
                "T5_ar": ybrown,
                "T5_pm": black,
                "T6": black,
                "T7": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T2_al": black,
                "T2_ar": black,
                "T2_pl": black,
                "T2_pr": black,
                "T3": black,
                "T3_pl": yellow,
                "T3_pr": yellow,
                "T5_al": ybrown,
                "T5_am": black,
                "T5_ar": ybrown,
                "T5_pm": black,
                "T6": black,
                "T7": black,
            },
            {
                "head": yellow,
                "mesosoma": yellow,
                "scutum": black,
                "propodeum_m": black,
                "metasoma": yellow,
                "T3_a": black,
                "T3_pm": black,
                "T6": black,
                "T7": black,
            },
        ],
    },
    "vandykei": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ],
    },
    "vosnesenskii": {
        "queen": [
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
            }
        ],
        "worker": [
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
            }
        ],
        "male": [
            {
                "head": yellow,
                "mesosoma": ybrown,
                "pronotum": yellow,
                "mesosoma_pr": black,
                "mesosoma_pl": black,
                "metasoma": black,
                "T4": yellow,
                "T5_a": ybrown,
                "T5_am": black,
                "T5_p": yellow,
                "T5_pm": black,
            },
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "mesosoma_ar": ybrown,
                "mesosoma_al": ybrown,
                "metasoma": black,
                "T4": yellow,
                "T5_a": ybrown,
                "T5_am": black,
                "T5_p": yellow,
                "T5_pm": black,
            },
        ]
    },
    "caliginosus": {
        "queen": [
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
            },
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
                "T4_a": black,
            },
        ],
        "worker": [
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
            },
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
                "T4_a": black,
            },
        ],
        "male": [
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "propodeum": ybrown,
                "metasoma": black,
                "T4": yellow,
                "T5_p": yellow,
                "T5_pm": ybrown,
            },
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
            },
            {
                "head": yellow,
                "mesosoma": black,
                "pronotum": yellow,
                "metasoma": black,
                "T4": yellow,
                "T4_a": black,
            },
        ]
    },
}


def flatten(class_spec):
    classes = {}

    def rcr(node, parents):
        nonlocal classes
        if type(node) is dict:
            for name in node:
                val = node[name]
                if val is None:
                    classes[name] = parents
                elif type(val) is list:
                    chparents = parents + [name]
                    for chname in val:
                        classes[chname] = chparents
                elif type(val) is dict:
                    rcr(val, parents + [name])
        else:
            raise Exception("Wat this?")
    rcr(class_spec, [])
    return classes


def make_color_map(class_spec, colors, default_colors):
    flattened_classes = flatten(class_spec)
    id_to_color = {}
    for (path_id, parents) in flattened_classes.items():
        if path_id in colors:
            id_to_color[path_id] = colors[path_id]
        else:
            for parent in reversed(parents):
                if parent in colors:
                    id_to_color[path_id] = colors[parent]
                    break
            else:
                id_to_color[path_id] = default_colors[path_id]

    return id_to_color


def replace_colors(dom, class_spec, colors, default_colors):
    color_map = make_color_map(class_spec, colors, default_colors)

    def rcr(node):
        nonlocal color_map
        path_id = node.attrib.get("id")
        if path_id is not None and path_id in color_map:
            style = node.attrib.get("style")
            style_parts = style.split(";")
            fill_indeces = [i for i, x in enumerate(style_parts) if x.startswith("fill")]
            if fill_indeces:
                style_parts[fill_indeces[0]] = "fill:" + color_map[path_id]
            style = ";".join(style_parts)
            node.attrib["style"] = style

        for child in node:
            rcr(child)

    rcr(dom.getroot())



'''
svg = ET.parse("bumblebee_male.svg")
replace_colors(svg, male_classes, patterns["vancouverensis"]["male"][0], male_default_colors)
pathlib.Path("generated").mkdir(parents=True, exist_ok=True)
svg.write(f"template_male.svg")
'''

for (species, castes) in patterns.items():
    for (caste, caste_patterns) in castes.items():
        for i, caste_pattern in enumerate(caste_patterns):
            if caste == "male":
                svg = ET.parse("bumblebee_male.svg")
                spec = male_classes
                default_colors = male_default_colors
            else:
                svg = ET.parse("bumblebee_female.svg")
                spec = female_classes
                default_colors = female_default_colors
            replace_colors(svg, spec, caste_pattern, default_colors)
            pathlib.Path("generated").mkdir(parents=True, exist_ok=True)
            svg.write(f"generated/{species}_{caste}{i}.svg")

