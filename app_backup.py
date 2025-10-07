#!/usr/bin/env python3
"""
Operational Memory Training System (OMTS)
Classified intelligence training program for developing photographic memory
and rapid visual intelligence gathering capabilities for field operatives.

Developed for: Intelligence agencies, deep cover operatives, and intelligence career preparation
Classification: Training Use Only
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import time
from datetime import datetime
import json
import os


class OperationalMemoryTraining:
    """Main application class for intelligence operative memory training."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("OMTS - Operational Memory Training System")
        self.root.geometry("1000x750")
        self.root.configure(bg='#0a0e1a')
        
        # User statistics
        self.stats_file = "memory_stats.json"
        self.stats = self.load_stats()
        
        # Current game state
        self.current_game = None
        self.score = 0
        self.level = 1
        
        # Create main menu
        self.create_main_menu()
    
    def load_stats(self):
        """Load user statistics from file."""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r') as f:
                    return json.load(f)
            except:
                return self.init_stats()
        return self.init_stats()
    
    def init_stats(self):
        """Initialize statistics structure."""
        return {
            'document_recall': {'played': 0, 'best_score': 0, 'total_score': 0},
            'license_plates': {'played': 0, 'best_score': 0, 'total_score': 0},
            'face_recognition': {'played': 0, 'best_score': 0, 'total_score': 0},
            'safe_combinations': {'played': 0, 'best_score': 0, 'total_score': 0},
            'surveillance_details': {'played': 0, 'best_score': 0, 'total_score': 0},
            'map_memorization': {'played': 0, 'best_score': 0, 'total_score': 0},
        }
    
    def save_stats(self):
        """Save user statistics to file."""
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)
    
    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_main_menu(self):
        """Create the main menu interface."""
        self.clear_window()
        
        # Title
        title_frame = tk.Frame(self.root, bg='#0a0e1a')
        title_frame.pack(pady=20)
        
        # Classification banner
        classification = tk.Label(
            title_frame,
            text="[TRAINING USE ONLY]",
            font=('Courier', 10, 'bold'),
            bg='#1a1f2e',
            fg='#ff6b6b',
            padx=10,
            pady=3
        )
        classification.pack(pady=(0, 10))
        
        title = tk.Label(
            title_frame,
            text="OPERATIONAL MEMORY TRAINING SYSTEM",
            font=('Courier', 28, 'bold'),
            bg='#0a0e1a',
            fg='#00ff41'
        )
        title.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Intelligence Operative Photographic Memory Development",
            font=('Courier', 12),
            bg='#0a0e1a',
            fg='#7d8590'
        )
        subtitle.pack(pady=5)
        
        version = tk.Label(
            title_frame,
            text="v2.0 | CLASSIFIED TRAINING MODULE",
            font=('Courier', 9),
            bg='#0a0e1a',
            fg='#4a5568'
        )
        version.pack(pady=2)
        
        # Game selection frame
        games_frame = tk.Frame(self.root, bg='#0a0e1a')
        games_frame.pack(pady=15, padx=50, fill='both', expand=True)
        
        # Mission briefing
        briefing = tk.Label(
            games_frame,
            text="SELECT TRAINING MODULE:",
            font=('Courier', 11, 'bold'),
            bg='#0a0e1a',
            fg='#7d8590'
        )
        briefing.pack(pady=(0, 10))
        
        # Game buttons
        games = [
            ("[M1] DOCUMENT RECALL", "Memorize classified documents & access codes", self.start_document_recall_game),
            ("[M2] LICENSE PLATE TRACKING", "Vehicle identification & surveillance", self.start_license_plate_game),
            ("[M3] FACE RECOGNITION", "Rapid facial feature memorization", self.start_face_recognition_game),
            ("[M4] SAFE COMBINATIONS", "Multi-digit security code retention", self.start_safe_combination_game),
            ("[M5] SURVEILLANCE DETAILS", "Scene observation & change detection", self.start_surveillance_game),
            ("[M6] MAP MEMORIZATION", "Tactical route & location memory", self.start_map_memorization_game),
        ]
        
        for i, (title, desc, command) in enumerate(games):
            btn_frame = tk.Frame(games_frame, bg='#1a1f2e', relief='solid', bd=1)
            btn_frame.pack(pady=6, padx=20, fill='x')
            
            btn = tk.Button(
                btn_frame,
                text=title,
                font=('Courier', 13, 'bold'),
                bg='#2d3748',
                fg='#00ff41',
                activebackground='#3d4758',
                activeforeground='#00ff41',
                command=command,
                cursor='hand2',
                relief='flat',
                pady=8,
                anchor='w',
                padx=15
            )
            btn.pack(fill='x', padx=3, pady=3)
            
            desc_label = tk.Label(
                btn_frame,
                text=f"  └─ {desc}",
                font=('Courier', 9),
                bg='#1a1f2e',
                fg='#7d8590',
                anchor='w'
            )
            desc_label.pack(pady=(0, 5), padx=15)
        
        # Statistics button
        stats_btn = tk.Button(
            self.root,
            text="[VIEW TRAINING RECORDS]",
            font=('Courier', 11, 'bold'),
            bg='#1a1f2e',
            fg='#7d8590',
            command=self.show_statistics,
            cursor='hand2',
            relief='flat',
            pady=8
        )
        stats_btn.pack(pady=10)
    
    def show_statistics(self):
        """Display user statistics."""
        self.clear_window()
        
        # Title
        title = tk.Label(
            self.root,
            text="TRAINING PERFORMANCE RECORDS",
            font=('Courier', 22, 'bold'),
            bg='#0a0e1a',
            fg='#00ff41'
        )
        title.pack(pady=20)
        
        # Stats frame
        stats_frame = tk.Frame(self.root, bg='#0a0e1a')
        stats_frame.pack(pady=20, padx=50, fill='both', expand=True)
        
        game_names = {
            'document_recall': '[M1] Document Recall',
            'license_plates': '[M2] License Plate Tracking',
            'face_recognition': '[M3] Face Recognition',
            'safe_combinations': '[M4] Safe Combinations',
            'surveillance_details': '[M5] Surveillance Details',
            'map_memorization': '[M6] Map Memorization'
        }
        
        for game_key, game_name in game_names.items():
            stats = self.stats[game_key]
            avg_score = stats['total_score'] / stats['played'] if stats['played'] > 0 else 0
            
            game_frame = tk.Frame(stats_frame, bg='#1a1f2e', relief='solid', bd=1)
            game_frame.pack(pady=6, padx=20, fill='x')
            
            name_label = tk.Label(
                game_frame,
                text=game_name,
                font=('Courier', 12, 'bold'),
                bg='#1a1f2e',
                fg='#00ff41'
            )
            name_label.pack(pady=5)
            
            info_text = f"Missions: {stats['played']} | Best: {stats['best_score']} | Avg: {avg_score:.1f}"
            info_label = tk.Label(
                game_frame,
                text=info_text,
                font=('Courier', 10),
                bg='#1a1f2e',
                fg='#7d8590'
            )
            info_label.pack(pady=5)
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="[RETURN TO MAIN MENU]",
            font=('Courier', 11),
            bg='#1a1f2e',
            fg='#7d8590',
            command=self.create_main_menu,
            cursor='hand2',
            relief='flat',
            pady=8
        )
        back_btn.pack(pady=20)
    
    # ========== GAME 1: DOCUMENT RECALL ==========
    
    def start_document_recall_game(self):
        """Start the classified document recall training."""
        self.current_game = 'document_recall'
        self.score = 0
        self.level = 1
        self.document_recall_round()
    
    def document_recall_round(self):
        """Run a single round of document recall training."""
        self.clear_window()
        
        # Generate classified document code based on level
        code_length = 4 + self.level
        
        # Intelligence-style codes: mix of letters, numbers, and dashes
        segments = []
        if self.level <= 2:
            # Simple: ABC-123
            segments.append(''.join(random.choices(string.ascii_uppercase, k=3)))
            segments.append(''.join(random.choices(string.digits, k=3)))
        elif self.level <= 5:
            # Medium: AB12-CD34
            for _ in range(2):
                segments.append(''.join(random.choices(string.ascii_uppercase, k=2)) + 
                              ''.join(random.choices(string.digits, k=2)))
        else:
            # Advanced: A1B2-C3D4-E5F6
            for _ in range(min(3, 1 + self.level // 3)):
                seg = ''
                for _ in range(2):
                    seg += random.choice(string.ascii_uppercase) + random.choice(string.digits)
                segments.append(seg)
        
        self.current_code = '-'.join(segments)
        
        # Display time based on level (decreases as level increases)
        display_time = max(2500, 6000 - (self.level * 300))
        
        # Header
        header = tk.Label(
            self.root,
            text=f"[M1] DOCUMENT RECALL - LEVEL {self.level}",
            font=('Courier', 18, 'bold'),
            bg='#0a0e1a',
            fg='#00ff41'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"SCORE: {self.score}",
            font=('Courier', 12),
            bg='#0a0e1a',
            fg='#7d8590'
        )
        score_label.pack()
        
        # Mission briefing
        briefing_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=1)
        briefing_frame.pack(pady=15, padx=100, fill='x')
        
        briefing = tk.Label(
            briefing_frame,
            text="MISSION: Memorize the classified document code",
            font=('Courier', 10, 'bold'),
            bg='#1a1f2e',
            fg='#ff6b6b',
            pady=8
        )
        briefing.pack()
        
        # Document display
        doc_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        doc_frame.pack(pady=40)
        
        doc_header = tk.Label(
            doc_frame,
            text="[CLASSIFIED - EYES ONLY]",
            font=('Courier', 10, 'bold'),
            bg='#1a1f2e',
            fg='#ff6b6b',
            padx=20,
            pady=5
        )
        doc_header.pack()
        
        code_label = tk.Label(
            doc_frame,
            text=self.current_code,
            font=('Courier', 42, 'bold'),
            bg='#1a1f2e',
            fg='#00ff41',
            padx=50,
            pady=40
        )
        code_label.pack()
        
        doc_footer = tk.Label(
            doc_frame,
            text=f"CLEARANCE LEVEL: {self.level}",
            font=('Courier', 9),
            bg='#1a1f2e',
            fg='#7d8590',
            pady=5
        )
        doc_footer.pack()
        
        # Hide code after display time
        self.root.after(display_time, lambda: self.document_recall_input())
    
    def document_recall_input(self):
        """Get user input for document recall."""
        self.clear_window()
        
        # Header
        header = tk.Label(
            self.root,
            text=f"[M1] DOCUMENT RECALL - LEVEL {self.level}",
            font=('Courier', 18, 'bold'),
            bg='#0a0e1a',
            fg='#00ff41'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"SCORE: {self.score}",
            font=('Courier', 12),
            bg='#0a0e1a',
            fg='#7d8590'
        )
        score_label.pack()
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="ENTER CLASSIFIED CODE FROM MEMORY:",
            font=('Courier', 12, 'bold'),
            bg='#0a0e1a',
            fg='#ff6b6b'
        )
        instructions.pack(pady=30)
        
        # Input field
        input_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        input_frame.pack(pady=20)
        
        input_label = tk.Label(
            input_frame,
            text="CODE:",
            font=('Courier', 12, 'bold'),
            bg='#1a1f2e',
            fg='#7d8590',
            padx=10
        )
        input_label.pack(side='left', padx=10)
        
        self.document_entry = tk.Entry(
            input_frame,
            font=('Courier', 20, 'bold'),
            bg='#2d3748',
            fg='#00ff41',
            insertbackground='#00ff41',
            justify='center',
            width=25
        )
        self.document_entry.pack(side='left', pady=15, padx=10)
        self.document_entry.focus()
        
        # Submit button
        submit_btn = tk.Button(
            self.root,
            text="[SUBMIT CODE]",
            font=('Courier', 12, 'bold'),
            bg='#2d3748',
            fg='#00ff41',
            command=self.check_document_recall_answer,
            cursor='hand2',
            relief='flat',
            pady=12,
            padx=40
        )
        submit_btn.pack(pady=30)
        
        # Bind Enter key
        self.document_entry.bind('<Return>', lambda e: self.check_document_recall_answer())
    
    def check_document_recall_answer(self):
        """Check the user's answer for document recall."""
        user_answer = self.document_entry.get().strip().upper()
        
        if user_answer == self.current_code:
            self.score += self.level * 10
            self.level += 1
            self.show_result(True, f"VERIFIED! Code: {self.current_code}")
            self.root.after(2000, self.document_recall_round)
        else:
            self.show_result(False, f"ACCESS DENIED!\nCorrect code: {self.current_code}\nYour entry: {user_answer}")
            self.end_game('document_recall')
    
    # ========== GAME 2: LICENSE PLATE TRACKING ==========
    
    def start_license_plate_game(self):
        """Start the license plate surveillance training."""
        self.current_game = 'license_plates'
        self.score = 0
        self.level = 1
        self.license_plate_round()
    
    def license_plate_round(self):
        """Run a single round of license plate surveillance training."""
        self.clear_window()
        
        # Generate license plates based on level
        num_plates = min(2 + self.level, 8)
        self.license_plates = []
        
        for _ in range(num_plates):
            # Generate realistic license plate formats
            if random.random() < 0.5:
                # Format: ABC-1234
                plate = ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' + \
                       ''.join(random.choices(string.digits, k=4))
            else:
                # Format: 12-ABC-34
                plate = ''.join(random.choices(string.digits, k=2)) + '-' + \
                       ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' + \
                       ''.join(random.choices(string.digits, k=2))
            self.license_plates.append(plate)
        
        # Display time
        display_time = max(3000, 6000 - (self.level * 250))
        
        # Header
        header = tk.Label(
            self.root,
            text=f"[M2] LICENSE PLATE TRACKING - LEVEL {self.level}",
            font=('Courier', 18, 'bold'),
            bg='#0a0e1a',
            fg='#00ff41'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"SCORE: {self.score}",
            font=('Courier', 12),
            bg='#0a0e1a',
            fg='#7d8590'
        )
        score_label.pack()
        
        # Mission briefing
        briefing_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=1)
        briefing_frame.pack(pady=15, padx=100, fill='x')
        
        briefing = tk.Label(
            briefing_frame,
            text=f"MISSION: Memorize {num_plates} vehicle license plates",
            font=('Courier', 10, 'bold'),
            bg='#1a1f2e',
            fg='#ff6b6b',
            pady=8
        )
        briefing.pack()
        
        # Surveillance feed display
        feed_frame = tk.Frame(self.root, bg='#0a0e1a')
        feed_frame.pack(pady=20)
        
        feed_label = tk.Label(
            feed_frame,
            text="[SURVEILLANCE FEED - ACTIVE]",
            font=('Courier', 10, 'bold'),
            bg='#0a0e1a',
            fg='#ff6b6b'
        )
        feed_label.pack(pady=5)
        
        # Display plates
        plates_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        plates_frame.pack(pady=20)
        
        for i, plate in enumerate(self.license_plates):
            plate_container = tk.Frame(plates_frame, bg='#2d3748', relief='raised', bd=2)
            plate_container.pack(pady=8, padx=30)
            
            vehicle_label = tk.Label(
                plate_container,
                text=f"VEHICLE #{i+1}:",
                font=('Courier', 9),
                bg='#2d3748',
                fg='#7d8590',
                padx=10,
                pady=2
            )
            vehicle_label.pack()
            
            plate_label = tk.Label(
                plate_container,
                text=plate,
                font=('Courier', 24, 'bold'),
                bg='#2d3748',
                fg='#ffff00',
                padx=20,
                pady=10
            )
            plate_label.pack()
        
        # Hide plates after display time
        self.root.after(display_time, self.license_plate_input)
    
    def pattern_grid_input(self):
        """Get user input for pattern grid game."""
        self.clear_window()
        
        self.user_selected = set()
        
        # Header
        header = tk.Label(
            self.root,
            text=f"Pattern Grid - Level {self.level}",
            font=('Arial', 20, 'bold'),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        score_label.pack()
        
        instructions = tk.Label(
            self.root,
            text="Click the cells that were highlighted:",
            font=('Arial', 12),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        instructions.pack(pady=10)
        
        # Grid frame
        grid_frame = tk.Frame(self.root, bg='#1e1e2e')
        grid_frame.pack(pady=30)
        
        cell_size = min(80, 400 // self.grid_size)
        self.grid_buttons = {}
        
        def toggle_cell(i, j, btn):
            if (i, j) in self.user_selected:
                self.user_selected.remove((i, j))
                btn.configure(bg='#313244')
            else:
                self.user_selected.add((i, j))
                btn.configure(bg='#89b4fa')
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                btn = tk.Button(
                    grid_frame,
                    bg='#313244',
                    width=cell_size // 10,
                    height=cell_size // 20,
                    relief='raised',
                    bd=2,
                    cursor='hand2'
                )
                btn.configure(command=lambda i=i, j=j, b=btn: toggle_cell(i, j, b))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.grid_buttons[(i, j)] = btn
        
        # Submit button
        submit_btn = tk.Button(
            self.root,
            text="Submit Answer",
            font=('Arial', 14, 'bold'),
            bg='#45475a',
            fg='#cdd6f4',
            command=self.check_pattern_grid_answer,
            cursor='hand2',
            relief='flat',
            pady=10,
            padx=30
        )
        submit_btn.pack(pady=20)
    
    def check_pattern_grid_answer(self):
        """Check the user's answer for pattern grid game."""
        if self.user_selected == self.highlighted_positions:
            self.score += self.level * 10
            self.level += 1
            self.show_result(True, "Perfect! You remembered all the cells!")
            self.root.after(2000, self.pattern_grid_round)
        else:
            correct = len(self.user_selected & self.highlighted_positions)
            total = len(self.highlighted_positions)
            self.show_result(False, f"Not quite! You got {correct}/{total} cells correct.")
            self.end_game('pattern_grid')
    
    # ========== GAME 3: NUMBER SEQUENCE ==========
    
    def start_number_sequence_game(self):
        """Start the number sequence game."""
        self.current_game = 'number_sequence'
        self.score = 0
        self.level = 1
        self.number_sequence_round()
    
    def number_sequence_round(self):
        """Run a single round of number sequence game."""
        self.clear_window()
        
        # Generate sequence
        sequence_length = 3 + self.level
        self.number_sequence = random.sample(range(1, 100), sequence_length)
        
        display_time = max(2000, 4000 - (self.level * 200))
        
        # Header
        header = tk.Label(
            self.root,
            text=f"Number Sequence - Level {self.level}",
            font=('Arial', 20, 'bold'),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        score_label.pack()
        
        instructions = tk.Label(
            self.root,
            text="Memorize these numbers in order!",
            font=('Arial', 12),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        instructions.pack(pady=10)
        
        # Number display
        number_frame = tk.Frame(self.root, bg='#313244', relief='raised', bd=5)
        number_frame.pack(pady=50)
        
        numbers_text = '  '.join(str(n) for n in self.number_sequence)
        numbers_label = tk.Label(
            number_frame,
            text=numbers_text,
            font=('Courier', 36, 'bold'),
            bg='#313244',
            fg='#a6e3a1',
            padx=40,
            pady=40
        )
        numbers_label.pack()
        
        self.root.after(display_time, self.number_sequence_input)
    
    def number_sequence_input(self):
        """Get user input for number sequence game."""
        self.clear_window()
        
        # Header
        header = tk.Label(
            self.root,
            text=f"Number Sequence - Level {self.level}",
            font=('Arial', 20, 'bold'),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        score_label.pack()
        
        instructions = tk.Label(
            self.root,
            text="Enter the numbers in the same order (separated by spaces):",
            font=('Arial', 12),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        instructions.pack(pady=30)
        
        # Input field
        input_frame = tk.Frame(self.root, bg='#1e1e2e')
        input_frame.pack(pady=20)
        
        self.number_entry = tk.Entry(
            input_frame,
            font=('Courier', 20),
            bg='#313244',
            fg='#cdd6f4',
            insertbackground='#cdd6f4',
            justify='center',
            width=30
        )
        self.number_entry.pack(pady=10)
        self.number_entry.focus()
        
        # Submit button
        submit_btn = tk.Button(
            self.root,
            text="Submit Answer",
            font=('Arial', 14, 'bold'),
            bg='#45475a',
            fg='#cdd6f4',
            command=self.check_number_sequence_answer,
            cursor='hand2',
            relief='flat',
            pady=10,
            padx=30
        )
        submit_btn.pack(pady=20)
        
        self.number_entry.bind('<Return>', lambda e: self.check_number_sequence_answer())
    
    def check_number_sequence_answer(self):
        """Check the user's answer for number sequence game."""
        try:
            user_answer = [int(x.strip()) for x in self.number_entry.get().split()]
            
            if user_answer == self.number_sequence:
                self.score += self.level * 10
                self.level += 1
                self.show_result(True, f"Correct! The sequence was: {' '.join(map(str, self.number_sequence))}")
                self.root.after(2000, self.number_sequence_round)
            else:
                self.show_result(False, f"Wrong! The sequence was: {' '.join(map(str, self.number_sequence))}\nYou entered: {' '.join(map(str, user_answer))}")
                self.end_game('number_sequence')
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numbers separated by spaces.")
    
    # ========== GAME 4: WHAT'S MISSING ==========
    
    def start_whats_missing_game(self):
        """Start the what's missing game."""
        self.current_game = 'whats_missing'
        self.score = 0
        self.level = 1
        self.whats_missing_round()
    
    def whats_missing_round(self):
        """Run a single round of what's missing game."""
        self.clear_window()
        
        # Generate items
        num_items = min(5 + self.level, 15)
        emojis = ['🍎', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍒', '🍑', '🥝',
                  '🥑', '🍆', '🥕', '🌽', '🥒', '🥦', '🍄', '🥜', '🌰', '🍞']
        
        self.items = random.sample(emojis, num_items)
        self.missing_item = random.choice(self.items)
        
        display_time = max(3000, 6000 - (self.level * 200))
        
        # Header
        header = tk.Label(
            self.root,
            text=f"What's Missing? - Level {self.level}",
            font=('Arial', 20, 'bold'),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        score_label.pack()
        
        instructions = tk.Label(
            self.root,
            text="Memorize all the items!",
            font=('Arial', 12),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        instructions.pack(pady=10)
        
        # Items display
        items_frame = tk.Frame(self.root, bg='#313244', relief='raised', bd=5)
        items_frame.pack(pady=30, padx=50)
        
        items_text = '  '.join(self.items)
        items_label = tk.Label(
            items_frame,
            text=items_text,
            font=('Arial', 32),
            bg='#313244',
            fg='#cdd6f4',
            padx=30,
            pady=30,
            wraplength=700
        )
        items_label.pack()
        
        self.root.after(display_time, self.whats_missing_input)
    
    def whats_missing_input(self):
        """Get user input for what's missing game."""
        self.clear_window()
        
        # Remove the missing item
        remaining_items = [item for item in self.items if item != self.missing_item]
        random.shuffle(remaining_items)
        
        # Header
        header = tk.Label(
            self.root,
            text=f"What's Missing? - Level {self.level}",
            font=('Arial', 20, 'bold'),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        score_label.pack()
        
        instructions = tk.Label(
            self.root,
            text="Which item is missing?",
            font=('Arial', 12),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        instructions.pack(pady=10)
        
        # Items display
        items_frame = tk.Frame(self.root, bg='#313244', relief='raised', bd=5)
        items_frame.pack(pady=20, padx=50)
        
        items_text = '  '.join(remaining_items)
        items_label = tk.Label(
            items_frame,
            text=items_text,
            font=('Arial', 32),
            bg='#313244',
            fg='#cdd6f4',
            padx=30,
            pady=30,
            wraplength=700
        )
        items_label.pack()
        
        # Choice buttons
        choices_frame = tk.Frame(self.root, bg='#1e1e2e')
        choices_frame.pack(pady=30)
        
        # Create choices (missing item + 3 random others)
        all_choices = [self.missing_item]
        other_items = [item for item in self.items if item != self.missing_item]
        all_choices.extend(random.sample(other_items, min(3, len(other_items))))
        random.shuffle(all_choices)
        
        for choice in all_choices:
            btn = tk.Button(
                choices_frame,
                text=choice,
                font=('Arial', 28),
                bg='#45475a',
                fg='#cdd6f4',
                command=lambda c=choice: self.check_whats_missing_answer(c),
                cursor='hand2',
                relief='flat',
                padx=20,
                pady=10
            )
            btn.pack(side='left', padx=10)
    
    def check_whats_missing_answer(self, choice):
        """Check the user's answer for what's missing game."""
        if choice == self.missing_item:
            self.score += self.level * 10
            self.level += 1
            self.show_result(True, f"Correct! The missing item was: {self.missing_item}")
            self.root.after(2000, self.whats_missing_round)
        else:
            self.show_result(False, f"Wrong! The missing item was: {self.missing_item}")
            self.end_game('whats_missing')
    
    # ========== GAME 5: COLOR SEQUENCE ==========
    
    def start_color_sequence_game(self):
        """Start the color sequence game."""
        self.current_game = 'color_sequence'
        self.score = 0
        self.level = 1
        self.color_sequence_round()
    
    def color_sequence_round(self):
        """Run a single round of color sequence game."""
        self.clear_window()
        
        # Color options
        self.colors = {
            'Red': '#f38ba8',
            'Blue': '#89b4fa',
            'Green': '#a6e3a1',
            'Yellow': '#f9e2af',
            'Purple': '#cba6f7',
            'Orange': '#fab387'
        }
        
        # Generate sequence
        sequence_length = 3 + self.level
        self.color_sequence = [random.choice(list(self.colors.keys())) for _ in range(sequence_length)]
        
        # Header
        header = tk.Label(
            self.root,
            text=f"Color Sequence - Level {self.level}",
            font=('Arial', 20, 'bold'),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        score_label.pack()
        
        instructions = tk.Label(
            self.root,
            text="Watch the color sequence carefully!",
            font=('Arial', 12),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        instructions.pack(pady=10)
        
        # Display frame
        display_frame = tk.Frame(self.root, bg='#1e1e2e')
        display_frame.pack(pady=50)
        
        self.color_display_label = tk.Label(
            display_frame,
            text="",
            font=('Arial', 24, 'bold'),
            bg='#313244',
            width=15,
            height=8,
            relief='raised',
            bd=5
        )
        self.color_display_label.pack()
        
        # Animate sequence
        self.animate_color_sequence(0)
    
    def animate_color_sequence(self, index):
        """Animate the color sequence display."""
        if index < len(self.color_sequence):
            color_name = self.color_sequence[index]
            color_hex = self.colors[color_name]
            
            self.color_display_label.configure(bg=color_hex, text=color_name)
            
            # Show each color for 1 second
            self.root.after(1000, lambda: self.color_display_label.configure(bg='#313244', text=''))
            self.root.after(1500, lambda: self.animate_color_sequence(index + 1))
        else:
            # Sequence complete, get user input
            self.root.after(500, self.color_sequence_input)
    
    def color_sequence_input(self):
        """Get user input for color sequence game."""
        self.clear_window()
        
        self.user_color_sequence = []
        
        # Header
        header = tk.Label(
            self.root,
            text=f"Color Sequence - Level {self.level}",
            font=('Arial', 20, 'bold'),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        header.pack(pady=20)
        
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        score_label.pack()
        
        instructions = tk.Label(
            self.root,
            text="Click the colors in the correct order:",
            font=('Arial', 12),
            bg='#1e1e2e',
            fg='#cdd6f4'
        )
        instructions.pack(pady=10)
        
        # User sequence display
        self.sequence_display = tk.Label(
            self.root,
            text="Your sequence: ",
            font=('Arial', 14),
            bg='#1e1e2e',
            fg='#a6adc8'
        )
        self.sequence_display.pack(pady=10)
        
        # Color buttons
        buttons_frame = tk.Frame(self.root, bg='#1e1e2e')
        buttons_frame.pack(pady=30)
        
        def add_color(color_name):
            self.user_color_sequence.append(color_name)
            self.sequence_display.configure(text=f"Your sequence: {' → '.join(self.user_color_sequence)}")
            
            if len(self.user_color_sequence) == len(self.color_sequence):
                self.root.after(500, self.check_color_sequence_answer)
        
        row = 0
        col = 0
        for color_name, color_hex in self.colors.items():
            btn = tk.Button(
                buttons_frame,
                text=color_name,
                font=('Arial', 14, 'bold'),
                bg=color_hex,
                fg='#1e1e2e',
                command=lambda c=color_name: add_color(c),
                cursor='hand2',
                relief='raised',
                bd=3,
                width=10,
                height=2
            )
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Reset button
        reset_btn = tk.Button(
            self.root,
            text="Reset",
            font=('Arial', 12),
            bg='#45475a',
            fg='#cdd6f4',
            command=lambda: self.reset_color_sequence(),
            cursor='hand2',
            relief='flat',
            pady=5,
            padx=20
        )
        reset_btn.pack(pady=10)
    
    def reset_color_sequence(self):
        """Reset the user's color sequence input."""
        self.user_color_sequence = []
        self.sequence_display.configure(text="Your sequence: ")
    
    def check_color_sequence_answer(self):
        """Check the user's answer for color sequence game."""
        if self.user_color_sequence == self.color_sequence:
            self.score += self.level * 10
            self.level += 1
            self.show_result(True, f"Perfect! The sequence was: {' → '.join(self.color_sequence)}")
            self.root.after(2000, self.color_sequence_round)
        else:
            self.show_result(False, f"Wrong! The sequence was: {' → '.join(self.color_sequence)}\nYou entered: {' → '.join(self.user_color_sequence)}")
            self.end_game('color_sequence')
    
    # ========== UTILITY FUNCTIONS ==========
    
    def show_result(self, is_correct, message):
        """Show result overlay."""
        overlay = tk.Frame(self.root, bg='#1e1e2e')
        overlay.place(relx=0.5, rely=0.5, anchor='center')
        
        result_frame = tk.Frame(overlay, bg='#313244', relief='raised', bd=5)
        result_frame.pack(padx=50, pady=50)
        
        emoji = "✅" if is_correct else "❌"
        color = '#a6e3a1' if is_correct else '#f38ba8'
        
        result_label = tk.Label(
            result_frame,
            text=f"{emoji}\n{message}",
            font=('Arial', 16, 'bold'),
            bg='#313244',
            fg=color,
            padx=40,
            pady=30,
            justify='center'
        )
        result_label.pack()
    
    def end_game(self, game_type):
        """End the current game and show final score."""
        # Update statistics
        self.stats[game_type]['played'] += 1
        self.stats[game_type]['total_score'] += self.score
        if self.score > self.stats[game_type]['best_score']:
            self.stats[game_type]['best_score'] = self.score
        self.save_stats()
        
        # Show final score after delay
        self.root.after(3000, self.show_final_score)
    
    def show_final_score(self):
        """Show final score screen."""
        self.clear_window()
        
        # Title
        title = tk.Label(
            self.root,
            text="Game Over!",
            font=('Arial', 32, 'bold'),
            bg='#1e1e2e',
            fg='#f38ba8'
        )
        title.pack(pady=40)
        
        # Score
        score_frame = tk.Frame(self.root, bg='#313244', relief='raised', bd=5)
        score_frame.pack(pady=20)
        
        final_score = tk.Label(
            score_frame,
            text=f"Final Score: {self.score}\nLevel Reached: {self.level}",
            font=('Arial', 24, 'bold'),
            bg='#313244',
            fg='#cdd6f4',
            padx=50,
            pady=30
        )
        final_score.pack()
        
        # Best score
        if self.current_game:
            best = self.stats[self.current_game]['best_score']
            best_label = tk.Label(
                self.root,
                text=f"Your Best: {best}",
                font=('Arial', 16),
                bg='#1e1e2e',
                fg='#a6adc8'
            )
            best_label.pack(pady=10)
        
        # Buttons
        btn_frame = tk.Frame(self.root, bg='#1e1e2e')
        btn_frame.pack(pady=30)
        
        play_again_btn = tk.Button(
            btn_frame,
            text="Play Again",
            font=('Arial', 14, 'bold'),
            bg='#45475a',
            fg='#cdd6f4',
            command=self.restart_current_game,
            cursor='hand2',
            relief='flat',
            pady=10,
            padx=30
        )
        play_again_btn.pack(side='left', padx=10)
        
        menu_btn = tk.Button(
            btn_frame,
            text="Main Menu",
            font=('Arial', 14, 'bold'),
            bg='#45475a',
            fg='#cdd6f4',
            command=self.create_main_menu,
            cursor='hand2',
            relief='flat',
            pady=10,
            padx=30
        )
        menu_btn.pack(side='left', padx=10)
    
    def restart_current_game(self):
        """Restart the current game."""
        if self.current_game == 'flashcard':
            self.start_flashcard_game()
        elif self.current_game == 'pattern_grid':
            self.start_pattern_grid_game()
        elif self.current_game == 'number_sequence':
            self.start_number_sequence_game()
        elif self.current_game == 'whats_missing':
            self.start_whats_missing_game()
        elif self.current_game == 'color_sequence':
            self.start_color_sequence_game()


def main():
    """Main entry point."""
    root = tk.Tk()
    app = MemoryTrainingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
