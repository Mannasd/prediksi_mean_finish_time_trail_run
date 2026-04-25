import numpy as np


# ==============================
# CARBOHYDRATE (DURING RACE)
# ==============================

def carb_rate_by_duration(hours):
    if hours < 1:
        return 0
    elif hours < 2:
        return 30
    elif hours < 3:
        return 60
    else:
        return 90


def carb_rate_by_weight(weight_kg):
    return 0.7 * weight_kg  # g/hour


# ==============================
# HYDRATION
# ==============================

def hydration_recommendation(hours):
    """
    General endurance guideline:
    ~400–800 ml/hour tergantung kondisi
    """
    return {
        "per_hour_ml": "400–800 ml",
        "note": "Tambahkan elektrolit untuk race >2 jam"
    }


# ==============================
# PROTEIN (RECOVERY)
# ==============================

def protein_recommendation(weight_kg):
    """
    1.2 – 1.4 g/kg/day
    """
    low = 1.2 * weight_kg
    high = 1.4 * weight_kg

    return {
        "daily_range": f"{low:.0f}–{high:.0f} g/hari",
        "note": "Untuk recovery setelah race"
    }


# ==============================
# FAT (SUPPORT ENERGY)
# ==============================

def fat_recommendation(weight_kg):
    """
    ~1 g/kg/day
    """
    fat = 1.0 * weight_kg

    return {
        "daily": f"{fat:.0f} g/hari",
        "note": "20–35% total kalori"
    }


# ==============================
# CALORIE ESTIMATION
# ==============================

def calorie_estimation(weight_kg):
    """
    37–41 kcal/kg/day
    """
    low = 37 * weight_kg
    high = 41 * weight_kg

    return {
        "daily_range": f"{low:.0f}–{high:.0f} kcal",
        "note": "Menyesuaikan intensitas latihan"
    }


# ==============================
# MASTER FUNCTION
# ==============================

def get_nutrition_plan(hours, weight_kg=None):

    # ======================
    # CARBS
    # ======================
    base_rate = carb_rate_by_duration(hours)

    if weight_kg:
        personal_rate = carb_rate_by_weight(weight_kg)
        carb_rate = (base_rate + personal_rate) / 2
    else:
        carb_rate = base_rate

    total_carb = carb_rate * hours

    # ======================
    # BUILD OUTPUT
    # ======================
    result = {
        "carbs": {
            "per_hour": round(carb_rate, 1),
            "total": round(total_carb, 0),
            "note": generate_carb_note(hours)
        },
        "hydration": hydration_recommendation(hours)
    }

    # optional (kalau weight ada)
    if weight_kg:
        result["protein"] = protein_recommendation(weight_kg)
        result["fat"] = fat_recommendation(weight_kg)
        result["calories"] = calorie_estimation(weight_kg)

    return result


# ==============================
# NOTE GENERATOR
# ==============================

def generate_carb_note(hours):
    if hours < 1:
        return "Cukup hidrasi"
    elif hours < 3:
        return "Gunakan gel/minuman karbohidrat"
    else:
        return "Gunakan kombinasi glucose + fructose untuk optimal absorption"