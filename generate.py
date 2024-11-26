import xml.etree.ElementTree as ET

black = "#292524"
orange = "#DB4B1A"
yellow = "#C6D431"


patterns = {
    "vosnesenskii": {
        "queen": [
            {
                "scutum_lr": black,
                "metasoma_al": black,
                "metasoma_pl": black,
                "metasoma_ar": black,
                "metasoma_pr": black,
                "T1_l": black,
                "T1_m": black,
                "T1_r": black,
                "T2_al": black,
                "T2_am": black,
                "T2_ar": black,
                "T2_pl": black,
                "T2_pm": black,
                "T2_pr": black,
                "T3_al": black,
                "T3_am": black,
                "T3_ar": black,
                "T3_pl": black,
                "T3_pm": black,
                "T3_pr": black,
                "T5_al": black,
                "T5_am": black,
                "T5_ar": black,
                "T5_pl": black,
                "T5_pm": black,
                "T5_pr": black,
            }
        ],
        "worker": [
        ],
        "male": [
        ]
    },
    "caliginosus": {
        "queen": [
        ],
        "worker": [
        ],
        "male": [
        ]
    },
}

def replace_colors(dom, colors):

    def rcr(node):
        path_id = node.attrib.get("id")
        if path_id is not None and path_id in colors:
            style = node.attrib.get("style")
            style_parts = style.split(";")
            fill_indeces = [i for i, x in enumerate(style_parts) if x.startswith("fill")]
            if fill_indeces:
                style_parts[fill_indeces[0]] = "fill:" + colors[path_id]
            style = ";".join(style_parts)
            node.attrib["style"] = style


        for child in node:
            rcr(child)

    rcr(dom.getroot())


for (species, castes) in patterns:
    for (caste, caste_patterns) in castes:
        for i, caste_pattern in enumerate(caste_patterns):
            if caste == "male":
                svg = ET.parse("bumblebee_male.svg")
            else:
                svg = ET.parse("bumblebee_female.svg")
            replace_colors(svg, caste_pattern)
            svg.write(f"{species}_{caste}{i}.svg")

