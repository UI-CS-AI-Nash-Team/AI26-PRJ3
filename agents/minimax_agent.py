class MinimaxAgent:
    def __init__(self, depth=4):
        self.depth = depth

    def evaluate(self, game, player):
        """
        تابع ارزیابی وضعیت بازی برای بازیکن player
        معیارها: کنترل گوشه‌ها + تحرک‌پذیری + تفاوت مهره‌ها
        """
        # اگر بازی تمام شده باشد، نتیجه نهایی را برمی‌گردانیم
        if game.game_over():
            b, w = game.score()
            my_score = b if player == 1 else w
            opp_score = w if player == 1 else b
            if my_score > opp_score:
                return 10000
            elif my_score < opp_score:
                return -10000
            else:
                return 0

        # 1) تفاوت تعداد مهره‌ها
        b, w = game.score()
        my_pieces = b if player == 1 else w
        opp_pieces = w if player == 1 else b
        piece_diff = my_pieces - opp_pieces

        # 2) تحرک‌پذیری (تعداد حرکات قانونی)
        my_moves = len(game.get_valid_moves(player))
        opp_moves = len(game.get_valid_moves(-player))
        mobility_diff = my_moves - opp_moves

        # 3) کنترل گوشه‌ها
        size = game.size
        corners = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]
        my_corners = 0
        opp_corners = 0
        for r, c in corners:
            if game.board[r][c] == player:
                my_corners += 1
            elif game.board[r][c] == -player:
                opp_corners += 1
        corner_diff = my_corners - opp_corners

        # ترکیب وزن‌دار معیارها
        score = (10 * corner_diff) + (5 * mobility_diff) + (1 * piece_diff)
        return score

    def minimax(self, game, depth, maximizing, root_player):
        """
        الگوریتم Minimax
        خروجی: یک tuple به صورت (value, best_move)
        """
        # شرط توقف: رسیدن به عمق صفر یا پایان بازی
        if depth == 0 or game.game_over():
            return self.evaluate(game, root_player), None

        current_player = root_player if maximizing else -root_player
        moves = game.get_valid_moves(current_player)

        # اگر بازیکن حرکت قانونی ندارد، نوبت پاس داده می‌شود
        if not moves:
            return self.minimax(game, depth - 1, not maximizing, root_player)

        best_move = moves[0]

        if maximizing:
            best_value = float('-inf')
            for move in moves:
                g = game.copy()
                g.make_move(current_player, *move)
                value, _ = self.minimax(g, depth - 1, False, root_player)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        else:
            best_value = float('inf')
            for move in moves:
                g = game.copy()
                g.make_move(current_player, *move)
                value, _ = self.minimax(g, depth - 1, True, root_player)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move

    def choose_move(self, game, player):
        value, move = self.minimax(game, self.depth, True, player)
        return move
