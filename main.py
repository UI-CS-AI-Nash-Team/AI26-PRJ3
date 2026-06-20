"""
University: University of Isfahan
Faculty: Mathematics and Statistics
Department: Computer Science
Course: Artificial Intelligence
Professor: Dr. Faria Nasiri Mofakham
TAs: MehrAzin Marzough, Mohammad Karimi, Anahita Honarmandian
Project: Adversarial Search in Othello (Minimax and Alpha-Beta Pruning)
"""
from agents.random_agent import RandomAgent
from agents.greedy_agent import GreedyAgent
from agents.minimax_agent import MinimaxAgent
from agents.alphabeta_agent import AlphaBetaAgent
from tournament import play_game
import time


def run_match(agent1, agent2, num_games=20):
    """Run num_games between two agents and count results"""
    a1_wins = 0
    a2_wins = 0
    draws = 0

    for i in range(num_games):
        # Alternate colors for fairness
        if i % 2 == 0:
            score = play_game(agent1, agent2)
        else:
            score = play_game(agent2, agent1)

        b_score, w_score = score
        if i % 2 == 0:
            my_score, opp_score = b_score, w_score
        else:
            my_score, opp_score = w_score, b_score

        if my_score > opp_score:
            a1_wins += 1
        elif my_score < opp_score:
            a2_wins += 1
        else:
            draws += 1

    return a1_wins, a2_wins, draws


if __name__ == "__main__":
    print("=" * 60)
    print("Testing MinimaxAgent vs RandomAgent")
    print("=" * 60)
    
    for depth in [2, 3, 4]:
        print(f"\n--- Search Depth: {depth} ---")
        start = time.time()
        wins, losses, draws = run_match(MinimaxAgent(depth=depth), RandomAgent(), 20)
        elapsed = time.time() - start
        print(f"Minimax(depth={depth}) Wins: {wins} | Losses: {losses} | Draws: {draws}")
        print(f"Win Rate: {(wins/20)*100:.1f}% | Time: {elapsed:.2f} seconds")

    print("\n" + "=" * 60)
    print("Testing MinimaxAgent vs GreedyAgent")
    print("=" * 60)
    
    for depth in [2, 3, 4]:
        print(f"\n--- Search Depth: {depth} ---")
        start = time.time()
        wins, losses, draws = run_match(MinimaxAgent(depth=depth), GreedyAgent(), 20)
        elapsed = time.time() - start
        print(f"Minimax(depth={depth}) Wins: {wins} | Losses: {losses} | Draws: {draws}")
        print(f"Win Rate: {(wins/20)*100:.1f}% | Time: {elapsed:.2f} seconds")

    print("\n" + "=" * 60)
    print("Testing AlphaBetaAgent vs RandomAgent")
    print("=" * 60)
    
    for depth in [3, 4, 5]:
        print(f"\n--- Search Depth: {depth} ---")
        start = time.time()
        wins, losses, draws = run_match(AlphaBetaAgent(depth=depth), RandomAgent(), 20)
        elapsed = time.time() - start
        print(f"AlphaBeta(depth={depth}) Wins: {wins} | Losses: {losses} | Draws: {draws}")
        print(f"Win Rate: {(wins/20)*100:.1f}% | Time: {elapsed:.2f} seconds")

    print("\n" + "=" * 60)
    print("Testing AlphaBetaAgent vs GreedyAgent")
    print("=" * 60)
    
    for depth in [3, 4, 5]:
        print(f"\n--- Search Depth: {depth} ---")
        start = time.time()
        wins, losses, draws = run_match(AlphaBetaAgent(depth=depth), GreedyAgent(), 20)
        elapsed = time.time() - start
        print(f"AlphaBeta(depth={depth}) Wins: {wins} | Losses: {losses} | Draws: {draws}")
        print(f"Win Rate: {(wins/20)*100:.1f}% | Time: {elapsed:.2f} seconds")

    print("\n" + "=" * 60)
    print("Comparing Minimax vs AlphaBeta (both depth 3) vs GreedyAgent")
    print("=" * 60)
    
    print("\n--- Minimax(depth=3) ---")
    start = time.time()
    w1, l1, d1 = run_match(MinimaxAgent(depth=3), GreedyAgent(), 20)
    t1 = time.time() - start
    print(f"Wins: {w1} | Losses: {l1} | Draws: {d1} | Time: {t1:.2f} seconds")
    
    print("\n--- AlphaBeta(depth=3) ---")
    start = time.time()
    w2, l2, d2 = run_match(AlphaBetaAgent(depth=3), GreedyAgent(), 20)
    t2 = time.time() - start
    print(f"Wins: {w2} | Losses: {l2} | Draws: {d2} | Time: {t2:.2f} seconds")
    
    print(f"\nResult: AlphaBeta is {(t1/t2):.2f}x faster than Minimax")
