def calculate_experience_points(game_mode, missions_completed, difficulty):
    if game_mode == "campaign":
        if difficulty == "easy":
            xp_per_mission = 50
        elif difficulty == "normal":
            xp_per_mission = 85
        elif difficulty == "hard":
            xp_per_mission = 150
        else:
            return "Error"
    elif game_mode == "multiplayer":
        if difficulty == "easy":
            xp_per_mission = 30
        elif difficulty == "normal":
            xp_per_mission = 55
        elif difficulty == "hard":
            xp_per_mission = 95
        else:
            return "Error"
    elif game_mode == "tutorial":
        if difficulty == "easy":
            xp_per_mission = 15
        elif difficulty == "normal":
            xp_per_mission = 25
        elif difficulty == "hard":
            xp_per_mission = 40
        else:
            return "Error"
    else:
        return "Error"
    return missions_completed * xp_per_mission

def calculate_skill_rating(play_hours, baseline_score, current_score):
    expected_score = 1000 + (play_hours * 100)
    score_range = expected_score - baseline_score
    skill_percent = (current_score - baseline_score) / score_range * 100
    return skill_percent

def determine_player_rank(skill_percent):
    if skill_percent < 50:
        return "Bronze Rank"
    elif 50 <= skill_percent < 60:
        return "Silver Rank"
    elif 60 <= skill_percent < 70:
        return "Gold Rank"
    elif 70 <= skill_percent <= 85:
        return "Platinum Rank"
    elif 85 < skill_percent <= 100:
        return "Diamond Rank"
    else:
        return "Error"

def calculate_reward_coins(xp_points, missions, rank):
    if rank == "Bronze Rank":
        bonus = 0.5
    elif rank == "Silver Rank":
        bonus = 1.0
    elif rank == "Gold Rank":
        bonus = 1.2
    elif rank == "Platinum Rank":
        bonus = 1.5
    elif rank == "Diamond Rank":
        bonus = 1.8
    else:
        return "Error"

    base_coins = xp_points * 0.05 + missions * 2
    final_coins = base_coins * bonus
    return round(final_coins, 1)

def needs_practice_mode(gaming_days, total_missions, avg_skill):
    if gaming_days >= 6 and avg_skill < 50:
        return True
    elif total_missions < 100 and avg_skill < 60:
        return True
    elif gaming_days >= 4 and avg_skill < 40:
        return True
    else:
        return False

print("GAMING ACHIEVEMENT TRACKER")
def generate_achievement_summary(player_name, game_mode, missions, difficulty, play_hours, baseline_score, current_score, gaming_days):
    xp_points = calculate_experience_points(game_mode, missions, difficulty)
    skill_percent = calculate_skill_rating(play_hours, baseline_score, current_score)
    rank = determine_player_rank(skill_percent)
    coins = calculate_reward_coins(xp_points, missions, rank)
    practice_needed = needs_practice_mode(gaming_days, missions, skill_percent)

    print("="*40)
    print(f"Achievement Summary for: {player_name}")
    print("-"*40)
    print(f"Game Mode: {game_mode}")
    print(f"Missions Completed: {missions}")
    print(f"Difficulty: {difficulty}")
    print(f"Experience Points: {xp_points}")
    print("Skill Analysis:")
    print(f"  Play Hours: {play_hours}, Baseline: {baseline_score}, Current Score: {current_score}")
    print(f"  Skill Rating: {round(skill_percent, 1)}%")
    print(f"  Player Rank: {rank}")
    print(f"Reward Coins: {coins}")
    print(f"Gaming Days: {gaming_days}")
    print(f"Practice Mode Needed: {'Yes' if practice_needed else 'No'}\n")

generate_achievement_summary("Phoenix", "campaign", 45, "hard", 3, 800, 1150, 3)
generate_achievement_summary("Storm", "multiplayer", 60, "normal", 5, 900, 1300, 5)
generate_achievement_summary("Echo", "tutorial", 30, "easy", 8, 850, 950, 7)