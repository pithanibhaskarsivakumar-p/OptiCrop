"""
OptiCrop - Agricultural Knowledge Base
Metadata, agronomic guidelines, soil requirements, and farming recommendations for 22 crops.
"""

CROP_DETAILS = {
    "rice": {
        "common_name": "Rice (Paddy)",
        "scientific_name": "Oryza sativa",
        "category": "Cereal / Grain",
        "icon": "🌾",
        "optimal_climate": "Tropical and subtropical with high humidity and standing water.",
        "soil_type": "Clayey, alluvial, or heavy loams with high water-retention capacity.",
        "growing_season": "Kharif (Monsoon: June – November)",
        "water_requirement": "High (Standing water 5–10 cm during vegetative stage, 1500–2500 mm overall)",
        "agronomic_advice": (
            "Ensure proper puddling before transplanting to reduce percolation losses. "
            "Apply nitrogen in 3 split doses (basal, tillering, panicle initiation) to maximize grain yield."
        )
    },
    "maize": {
        "common_name": "Maize (Corn)",
        "scientific_name": "Zea mays",
        "category": "Cereal / Grain",
        "icon": "🌽",
        "optimal_climate": "Warm temperate to tropical climates with plenty of sunshine.",
        "soil_type": "Deep, fertile, well-drained loamy to sandy-loam soils rich in organic matter.",
        "growing_season": "Kharif & Rabi (adaptable throughout the year with adequate moisture)",
        "water_requirement": "Moderate (500–800 mm; critical periods: tasseling and silking)",
        "agronomic_advice": (
            "Avoid waterlogging at all stages. Ensure adequate phosphorus at sowing for strong root "
            "establishment and early cob development."
        )
    },
    "chickpea": {
        "common_name": "Chickpea (Gram)",
        "scientific_name": "Cicer arietinum",
        "category": "Pulse / Legume",
        "icon": "🧆",
        "optimal_climate": "Cool, dry subtropical weather during vegetative phase, warm during maturity.",
        "soil_type": "Well-drained sandy loam to clay loam; sensitive to excessive salinity and wet soil.",
        "growing_season": "Rabi (Winter: October – March)",
        "water_requirement": "Low (250–400 mm; drought tolerant, thrives on residual soil moisture)",
        "agronomic_advice": (
            "Inoculate seeds with Rhizobium culture prior to sowing to promote atmospheric nitrogen fixation. "
            "Avoid heavy nitrogenous fertilizers."
        )
    },
    "kidneybeans": {
        "common_name": "Kidney Beans (Rajma)",
        "scientific_name": "Phaseolus vulgaris",
        "category": "Pulse / Legume",
        "icon": "🫘",
        "optimal_climate": "Mild tropical to temperate climate, sensitive to both frost and intense heat.",
        "soil_type": "Well-drained light loams with organic matter; pH between 5.5 and 6.5.",
        "growing_season": "Kharif in hills; Rabi/late winter in plains",
        "water_requirement": "Moderate (400–600 mm; uniform moisture during pod development)",
        "agronomic_advice": (
            "Unlike other legumes, kidney beans fix minimal atmospheric nitrogen and therefore "
            "require balanced basal nitrogen and phosphorus application."
        )
    },
    "pigeonpeas": {
        "common_name": "Pigeonpeas (Arhar / Red Gram)",
        "scientific_name": "Cajanus cajan",
        "category": "Pulse / Legume",
        "icon": "🌱",
        "optimal_climate": "Semi-arid tropical climate with high drought tolerance.",
        "soil_type": "Deep, well-drained loam to heavy clay; tolerant to mild alkaline soils.",
        "growing_season": "Kharif (June/July to December/January)",
        "water_requirement": "Low to Moderate (600–700 mm; deep taproot extracts subsoil water)",
        "agronomic_advice": (
            "Ideal for intercropping with cotton, sorghum, or maize. "
            "Ensure field drainage to prevent phytophthora blight and root rot during monsoon."
        )
    },
    "mothbeans": {
        "common_name": "Moth Beans (Matki)",
        "scientific_name": "Vigna aconitifolia",
        "category": "Pulse / Legume",
        "icon": "🌿",
        "optimal_climate": "Extremely arid and semi-arid, high heat tolerance.",
        "soil_type": "Sandy, poor marginal soils; requires good drainage.",
        "growing_season": "Kharif (Rainy season, short-duration 65–85 days)",
        "water_requirement": "Very Low (200–350 mm; excellent drought resistance)",
        "agronomic_advice": (
            "Acts as excellent living mulch and soil cover to prevent soil erosion in arid tracts. "
            "Requires negligible chemical fertilizer."
        )
    },
    "mungbean": {
        "common_name": "Mung Bean (Green Gram)",
        "scientific_name": "Vigna radiata",
        "category": "Pulse / Legume",
        "icon": "🟢",
        "optimal_climate": "Warm, sunny weather (25–35°C); highly sensitive to frost.",
        "soil_type": "Well-drained fertile loamy to sandy-loam soils.",
        "growing_season": "Kharif, Spring, and Summer crop",
        "water_requirement": "Low to Moderate (350–500 mm; short maturity cycle of 60–75 days)",
        "agronomic_advice": (
            "Excellent catch crop between major cropping cycles. Fixes 30–50 kg atmospheric N/ha, "
            "substantially enriching following crop yields."
        )
    },
    "blackgram": {
        "common_name": "Black Gram (Urad)",
        "scientific_name": "Vigna mungo",
        "category": "Pulse / Legume",
        "icon": "⚫",
        "optimal_climate": "Hot and humid tropical climate (25–35°C).",
        "soil_type": "Loam to heavy soils with good moisture-retaining capacity.",
        "growing_season": "Kharif and Rabi seasons",
        "water_requirement": "Moderate (400–600 mm; avoid water logging)",
        "agronomic_advice": (
            "Foliar spray of 2% DAP at flower initiation boosts pod set. Keep fields free of weeds "
            "in the first 30 days."
        )
    },
    "lentil": {
        "common_name": "Lentil (Masoor)",
        "scientific_name": "Lens culinaris",
        "category": "Pulse / Legume",
        "icon": "🥣",
        "optimal_climate": "Cool weather during vegetative growth, warm dry weather at maturity.",
        "soil_type": "Alluvial, light loams, clayey soils; adaptable to low-fertility soils.",
        "growing_season": "Rabi (Winter: October – March)",
        "water_requirement": "Low (200–350 mm; tolerates drought well)",
        "agronomic_advice": (
            "Treat seed with Rhizobium and Trichoderma. Avoid excessive water near harvesting to "
            "prevent seed discoloration."
        )
    },
    "pomegranate": {
        "common_name": "Pomegranate",
        "scientific_name": "Punica granatum",
        "category": "Fruit / Horticulture",
        "icon": "🫐",
        "optimal_climate": "Semi-arid to arid with hot dry summers and cool winters.",
        "soil_type": "Deep loamy or alluvial soil, pH 6.5–7.5, excellent drainage essential.",
        "growing_season": "Perennial (Bahar treatment timed for winter, rainy, or summer harvest)",
        "water_requirement": "Moderate (Drip irrigation recommended; regulates aril development and prevents fruit cracking)",
        "agronomic_advice": (
            "Maintain regular micronutrient foliar sprays (Boron, Zinc, Calcium) to prevent fruit cracking "
            "and enhance sweetness and rind gloss."
        )
    },
    "banana": {
        "common_name": "Banana",
        "scientific_name": "Musa acuminata",
        "category": "Fruit / Commercial",
        "icon": "🍌",
        "optimal_climate": "Warm, humid tropical climate with uniform temperatures (20–35°C).",
        "soil_type": "Deep, fertile, well-drained alluvial or volcanic clay loam rich in potassium and humus.",
        "growing_season": "Planting throughout the year; 11–13 month crop cycle",
        "water_requirement": "Very High (1500–2200 mm; continuous moisture essential via drip fertigation)",
        "agronomic_advice": (
            "Heavy potassium feeder! Apply potash liberally from shooting stage onwards to enhance bunch weight, "
            "finger size, and shelf life."
        )
    },
    "mango": {
        "common_name": "Mango (King of Fruits)",
        "scientific_name": "Mangifera indica",
        "category": "Fruit / Horticulture",
        "icon": "🥭",
        "optimal_climate": "Tropical and subtropical with a dry season preceding flowering.",
        "soil_type": "Deep alluvial loams or red lateritic soils with good drainage; depth > 2m.",
        "growing_season": "Perennial tree crop (flowering in winter, harvesting in spring/summer)",
        "water_requirement": "Moderate (Withhold watering 2 months before flowering to induce flower bud differentiation)",
        "agronomic_advice": (
            "Prune inner dead branches after annual harvest to facilitate sunlight penetration. "
            "Spray paclobutrazol where regulated canopy and synchronized flowering are desired."
        )
    },
    "grapes": {
        "common_name": "Grapes",
        "scientific_name": "Vitis vinifera",
        "category": "Fruit / Horticulture",
        "icon": "🍇",
        "optimal_climate": "Warm, dry Mediterranean or semi-arid climate with high sunshine hours.",
        "soil_type": "Well-drained sandy loam to gravelly loam with high potassium reserves.",
        "growing_season": "Perennial (two prunings per year: forward/foundation and back pruning)",
        "water_requirement": "Moderate (600–800 mm; strictly controlled during fruit ripening to boost Brix/sugar levels)",
        "agronomic_advice": (
            "Train vines on Bower or Y-trellis for optimum ventilation and cluster sunlight exposure. "
            "Apply Gibberellic Acid (GA3) at bloom for berry elongation and bunch loosening."
        )
    },
    "watermelon": {
        "common_name": "Watermelon",
        "scientific_name": "Citrullus lanatus",
        "category": "Fruit / Cucurbit",
        "icon": "🍉",
        "optimal_climate": "Hot, dry sunny weather with long warm days (24–32°C).",
        "soil_type": "Sandy or sandy-loam soils along river beds or fields with rapid drainage.",
        "growing_season": "Summer (Zaid season: February – June)",
        "water_requirement": "Moderate to High (400–600 mm; reduce water near ripening to concentrate sugars)",
        "agronomic_advice": (
            "Use silver-black plastic mulch and drip fertigation to conserve soil moisture, prevent weed growth, "
            "and maintain unblemished rind coloration."
        )
    },
    "muskmelon": {
        "common_name": "Muskmelon (Cantaloupe)",
        "scientific_name": "Cucumis melo",
        "category": "Fruit / Cucurbit",
        "icon": "🍈",
        "optimal_climate": "Warm, dry conditions with high sunlight; frost sensitive.",
        "soil_type": "Sandy loam, rich in organic matter, pH 6.0–7.0.",
        "growing_season": "Summer (Zaid: February – May)",
        "water_requirement": "Moderate (300–500 mm; avoid wetting foliage to prevent downy mildew)",
        "agronomic_advice": (
            "Harvest at 'full slip' stage for maximum sweetness and aroma. Ensure high potassium "
            "feeding during fruit sizing."
        )
    },
    "apple": {
        "common_name": "Apple",
        "scientific_name": "Malus domestica",
        "category": "Fruit / Temperate",
        "icon": "🍎",
        "optimal_climate": "Temperate climate requiring 800–1200 hours of chilling (< 7°C) during winter.",
        "soil_type": "Deep, well-drained loamy soils rich in organic matter, slightly acidic (pH 5.5–6.8).",
        "growing_season": "Perennial (Spring bloom, late summer/autumn harvest)",
        "water_requirement": "Moderate (800–1200 mm evenly distributed throughout vegetative and fruit sizing)",
        "agronomic_advice": (
            "Ensure regular winter pruning and canopy thinning. Plant 10–15% pollinizer varieties "
            "(e.g., Crab apple or Golden Delicious) to ensure full cross-pollination."
        )
    },
    "orange": {
        "common_name": "Orange (Citrus)",
        "scientific_name": "Citrus sinensis",
        "category": "Fruit / Citrus",
        "icon": "🍊",
        "optimal_climate": "Subtropical to tropical with distinct dry and wet cycles.",
        "soil_type": "Light, well-aerated sandy loam with pH 6.0–7.5; zero water stagnation tolerance.",
        "growing_season": "Perennial (Ambe, Mrig, or Hasta bahar seasons)",
        "water_requirement": "Moderate (900–1200 mm; sensitive to water deficit during fruit set)",
        "agronomic_advice": (
            "Watch out for Citrus Canker and Citrus Greening. Apply micronutrients (Zinc, Iron, Manganese) "
            "quarterly to eliminate interveinal chlorosis."
        )
    },
    "papaya": {
        "common_name": "Papaya",
        "scientific_name": "Carica papaya",
        "category": "Fruit / Commercial",
        "icon": "🥭",
        "optimal_climate": "Tropical and warm subtropical, frost-free climate (21–33°C).",
        "soil_type": "Well-drained sandy loam or alluvial soil rich in organic matter; extremely susceptible to waterlogging.",
        "growing_season": "Planted year-round (except severe winter); fruiting in 9–10 months",
        "water_requirement": "Moderate to High (1000–1500 mm; steady soil moisture with drip lines)",
        "agronomic_advice": (
            "Even 24 hours of standing water can cause fatal root and collar rot. Mound-plant seedlings "
            "with efficient drainage channels."
        )
    },
    "coconut": {
        "common_name": "Coconut (Kalpavriksha)",
        "scientific_name": "Cocos nucifera",
        "category": "Plantation / Oilseed",
        "icon": "🥥",
        "optimal_climate": "Humid coastal tropical climate with warm temperatures and high sunlight.",
        "soil_type": "Coastal sandy soils, alluvial, or red laterite soils with good drainage.",
        "growing_season": "Perennial palm; continuous monthly flowering and nut yield",
        "water_requirement": "High (1300–2300 mm distributed evenly; thrives with brackish or coastal groundwater)",
        "agronomic_advice": (
            "High requirement of Sodium chloride (common salt) and Potassium for optimal nut production, "
            "kernel thickness, and disease resistance."
        )
    },
    "cotton": {
        "common_name": "Cotton (White Gold)",
        "scientific_name": "Gossypium hirsutum",
        "category": "Fiber / Cash Crop",
        "icon": "☁️",
        "optimal_climate": "Warm semi-arid to tropical climate with 180–200 frost-free days and bright sunshine.",
        "soil_type": "Deep black cotton soils (regur) with excellent moisture retention, or well-drained alluvial loam.",
        "growing_season": "Kharif (May/June sowing, harvesting October – January)",
        "water_requirement": "Moderate (600–1000 mm; dry spell needed during boll bursting and picking)",
        "agronomic_advice": (
            "Monitor for Pink Bollworm using pheromone traps. Avoid excessive nitrogen to prevent vegetative "
            "rank growth at the expense of boll formation."
        )
    },
    "jute": {
        "common_name": "Jute (Golden Fiber)",
        "scientific_name": "Corchorus capsularis",
        "category": "Fiber / Commercial",
        "icon": "🌾",
        "optimal_climate": "Hot and humid tropical monsoon climate (humidity > 70%, temp 24–37°C).",
        "soil_type": "New alluvial soils along river floodplains rich in silt deposits.",
        "growing_season": "Kharif (Sowing in March – May, harvesting 120 days after sowing)",
        "water_requirement": "High (1500–2000 mm; tolerant of waterlogged soils during later growth)",
        "agronomic_advice": (
            "Harvest at the small pod stage for the optimal balance between fiber yield and fiber tensile strength. "
            "Provide clean, slow-moving water for proper retting."
        )
    },
    "coffee": {
        "common_name": "Coffee (Arabica / Robusta)",
        "scientific_name": "Coffea arabica / canephora",
        "category": "Plantation / Beverage",
        "icon": "☕",
        "optimal_climate": "Subtropical highland or tropical shade canopy (15–28°C) with misty conditions.",
        "soil_type": "Deep, well-drained volcanic loams or forest soil rich in humus, acidic (pH 5.0–6.5).",
        "growing_season": "Perennial shade crop (harvesting November – February)",
        "water_requirement": "High (1500–2500 mm; blossom showers critical in March/April)",
        "agronomic_advice": (
            "Cultivate under a two-tier shade tree canopy (e.g., Silver Oak, Dalbergia). "
            "Ensure regular mulching with leaf litter to preserve root-zone humidity and suppress weeds."
        )
    }
}

def get_crop_metadata(crop_label: str) -> dict:
    normalized = crop_label.strip().lower()
    return CROP_DETAILS.get(normalized, {
        "common_name": crop_label.title(),
        "scientific_name": "N/A",
        "category": "Agricultural Crop",
        "icon": "🌱",
        "optimal_climate": "Standard agricultural conditions.",
        "soil_type": "Well-drained agricultural soil.",
        "growing_season": "Regular cropping season",
        "water_requirement": "Moderate",
        "agronomic_advice": "Consult local agricultural extension officers for region-specific guidelines."
    })
