#!/usr/bin/env python3
"""
Intelligence Memory Training
Develop photographic memory and rapid recall skills for intelligence work.
"""

import tkinter as tk
from tkinter import messagebox
import random
import string
import json
import os


class OperationalMemoryTraining:
    """Main application class for intelligence operative memory training."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligence Memory Training")
        self.root.geometry("1000x750")
        self.root.configure(bg='#0a0e1a')
        
        # User statistics
        self.stats_file = "omts_stats.json"
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
        title_frame.pack(pady=30)
        
        title = tk.Label(
            title_frame,
            text="Intelligence Memory Training",
            font=('Helvetica', 32, 'bold'),
            bg='#0a0e1a',
            fg='#00ff41'
        )
        title.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Develop photographic memory for intelligence work",
            font=('Helvetica', 13),
            bg='#0a0e1a',
            fg='#7d8590'
        )
        subtitle.pack(pady=8)
        
        # Game selection frame
        games_frame = tk.Frame(self.root, bg='#0a0e1a')
        games_frame.pack(pady=15, padx=50, fill='both', expand=True)
        
        # Game buttons
        games = [
            ("Document Codes", "Memorize access codes and document identifiers", self.start_document_recall),
            ("License Plates", "Track and recall vehicle identification numbers", self.start_license_plates),
            ("Face Recognition", "Remember faces and identifying features", self.start_face_recognition),
            ("Number Sequences", "Retain multi-digit codes and combinations", self.start_safe_combinations),
            ("Scene Details", "Observe and recall environmental details", self.start_surveillance),
            ("Route Memory", "Memorize directions and navigation sequences", self.start_map_memory),
        ]
        
        for i, (title, desc, command) in enumerate(games):
            btn_frame = tk.Frame(games_frame, bg='#1a1f2e', relief='solid', bd=1)
            btn_frame.pack(pady=5, padx=20, fill='x')
            
            btn = tk.Button(
                btn_frame,
                text=title,
                font=('Helvetica', 14, 'bold'),
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
                text=desc,
                font=('Helvetica', 10),
                bg='#1a1f2e',
                fg='#7d8590',
                anchor='w'
            )
            desc_label.pack(pady=(0, 5), padx=15)
        
        # Statistics button
        stats_btn = tk.Button(
            self.root,
            text="View Statistics",
            font=('Helvetica', 12),
            bg='#1a1f2e',
            fg='#7d8590',
            command=self.show_statistics,
            cursor='hand2',
            relief='flat',
            pady=10
        )
        stats_btn.pack(pady=15)
    
    def show_statistics(self):
        """Display user statistics."""
        self.clear_window()
        
        # Title
        title = tk.Label(
            self.root,
            text="Performance Statistics",
            font=('Helvetica', 28, 'bold'),
            bg='#0a0e1a',
            fg='#00ff41'
        )
        title.pack(pady=25)
        
        # Stats frame
        stats_frame = tk.Frame(self.root, bg='#0a0e1a')
        stats_frame.pack(pady=20, padx=50, fill='both', expand=True)
        
        game_names = {
            'document_recall': 'Document Codes',
            'license_plates': 'License Plates',
            'face_recognition': 'Face Recognition',
            'safe_combinations': 'Number Sequences',
            'surveillance_details': 'Scene Details',
            'map_memorization': 'Route Memory'
        }
        
        for game_key, game_name in game_names.items():
            stats = self.stats[game_key]
            avg_score = stats['total_score'] / stats['played'] if stats['played'] > 0 else 0
            
            game_frame = tk.Frame(stats_frame, bg='#1a1f2e', relief='solid', bd=1)
            game_frame.pack(pady=5, padx=20, fill='x')
            
            name_label = tk.Label(
                game_frame,
                text=game_name,
                font=('Helvetica', 13, 'bold'),
                bg='#1a1f2e',
                fg='#00ff41'
            )
            name_label.pack(pady=5)
            
            info_text = f"Sessions: {stats['played']} | Best: {stats['best_score']} | Average: {avg_score:.1f}"
            info_label = tk.Label(
                game_frame,
                text=info_text,
                font=('Helvetica', 10),
                bg='#1a1f2e',
                fg='#7d8590'
            )
            info_label.pack(pady=5)
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="← Back to Menu",
            font=('Helvetica', 12),
            bg='#1a1f2e',
            fg='#7d8590',
            command=self.create_main_menu,
            cursor='hand2',
            relief='flat',
            pady=10
        )
        back_btn.pack(pady=20)
    
    # ========== M1: DOCUMENT RECALL ==========
    
    def start_document_recall(self):
        """Start classified document recall training."""
        self.current_game = 'document_recall'
        self.score = 0
        self.level = 1
        self.document_recall_round()
    
    def document_recall_round(self):
        """Display classified document code."""
        self.clear_window()
        
        # Generate intelligence-style code
        segments = []
        if self.level <= 2:
            segments.append(''.join(random.choices(string.ascii_uppercase, k=3)))
            segments.append(''.join(random.choices(string.digits, k=3)))
        elif self.level <= 5:
            for _ in range(2):
                segments.append(''.join(random.choices(string.ascii_uppercase, k=2)) + 
                              ''.join(random.choices(string.digits, k=2)))
        else:
            for _ in range(min(3, 1 + self.level // 3)):
                seg = ''
                for _ in range(2):
                    seg += random.choice(string.ascii_uppercase) + random.choice(string.digits)
                segments.append(seg)
        
        self.current_code = '-'.join(segments)
        display_time = max(2500, 6000 - (self.level * 300))
        
        self._show_header("DOCUMENT RECALL", 1)
        
        briefing = tk.Label(
            self.root,
            text="Memorize the document code",
            font=('Helvetica', 12),
            bg='#0a0e1a',
            fg='#7d8590',
            pady=10
        )
        briefing.pack()
        
        doc_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        doc_frame.pack(pady=30)
        
        tk.Label(doc_frame, text=self.current_code, font=('Courier', 44, 'bold'),
                bg='#1a1f2e', fg='#00ff41', padx=50, pady=50).pack()
        
        self.root.after(display_time, lambda: self._get_text_input(
            "Enter the code from memory:",
            self.current_code,
            self.document_recall_round,
            'document_recall'
        ))
    
    # ========== M2: LICENSE PLATE TRACKING ==========
    
    def start_license_plates(self):
        """Start license plate surveillance training."""
        self.current_game = 'license_plates'
        self.score = 0
        self.level = 1
        self.license_plate_round()
    
    def license_plate_round(self):
        """Display license plates for memorization."""
        self.clear_window()
        
        num_plates = min(2 + self.level, 6)
        self.license_plates = []
        
        for _ in range(num_plates):
            if random.random() < 0.5:
                plate = ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' + \
                       ''.join(random.choices(string.digits, k=4))
            else:
                plate = ''.join(random.choices(string.digits, k=2)) + '-' + \
                       ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' + \
                       ''.join(random.choices(string.digits, k=2))
            self.license_plates.append(plate)
        
        display_time = max(3000, 6000 - (self.level * 250))
        
        self._show_header("LICENSE PLATE TRACKING", 2)
        
        tk.Label(self.root, text=f"Memorize {num_plates} license plates",
                font=('Helvetica', 12), bg='#0a0e1a', fg='#7d8590', pady=10).pack()
        
        plates_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        plates_frame.pack(pady=15)
        
        for i, plate in enumerate(self.license_plates):
            container = tk.Frame(plates_frame, bg='#2d3748', relief='raised', bd=2)
            container.pack(pady=6, padx=25)
            
            tk.Label(container, text=f"Vehicle {i+1}", font=('Helvetica', 10),
                    bg='#2d3748', fg='#7d8590', padx=10, pady=3).pack()
            
            tk.Label(container, text=plate, font=('Courier', 22, 'bold'),
                    bg='#2d3748', fg='#ffff00', padx=20, pady=8).pack()
        
        self.root.after(display_time, lambda: self._get_multiline_input(
            "Enter all license plates (one per line):",
            self.license_plates,
            self.license_plate_round,
            'license_plates'
        ))
    
    # ========== M3: FACE RECOGNITION ==========
    
    def start_face_recognition(self):
        """Start facial feature memorization training."""
        self.current_game = 'face_recognition'
        self.score = 0
        self.level = 1
        self.face_recognition_round()
    
    def face_recognition_round(self):
        """Display suspect profile for memorization."""
        self.clear_window()
        
        # Generate suspect profile
        first_names = ['ALEX', 'BLAKE', 'CASEY', 'DREW', 'ELLIS', 'FINLEY', 'GRAY', 'HARPER']
        last_names = ['ANDERSON', 'BROOKS', 'CARTER', 'DAVIS', 'EVANS', 'FOSTER', 'GRANT', 'HAYES']
        
        self.suspect_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        self.suspect_age = random.randint(25, 55)
        self.suspect_height = f"{random.randint(5,6)}'{random.randint(0,11)}\""
        
        features = ['SCAR ON LEFT CHEEK', 'TATTOO ON NECK', 'GLASSES', 'BEARD',
                   'BALD', 'LONG HAIR', 'EARRING', 'MUSTACHE']
        self.suspect_features = random.sample(features, min(2 + self.level // 2, 4))
        
        display_time = max(4000, 8000 - (self.level * 300))
        
        self._show_header("FACE RECOGNITION", 3)
        
        tk.Label(self.root, text="Memorize the suspect profile",
                font=('Helvetica', 12), bg='#0a0e1a', fg='#7d8590', pady=10).pack()
        
        profile_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        profile_frame.pack(pady=20)
        
        tk.Label(profile_frame, text="Suspect Profile",
                font=('Helvetica', 14, 'bold'), bg='#1a1f2e', fg='#00ff41', pady=8).pack()
        
        info_frame = tk.Frame(profile_frame, bg='#2d3748')
        info_frame.pack(pady=15, padx=30)
        
        tk.Label(info_frame, text=f"Name: {self.suspect_name}", font=('Helvetica', 15, 'bold'),
                bg='#2d3748', fg='#00ff41', anchor='w').pack(fill='x', pady=4)
        tk.Label(info_frame, text=f"Age: {self.suspect_age}", font=('Helvetica', 13),
                bg='#2d3748', fg='#7d8590', anchor='w').pack(fill='x', pady=2)
        tk.Label(info_frame, text=f"Height: {self.suspect_height}", font=('Helvetica', 13),
                bg='#2d3748', fg='#7d8590', anchor='w').pack(fill='x', pady=2)
        
        tk.Label(info_frame, text="Features:", font=('Helvetica', 13, 'bold'),
                bg='#2d3748', fg='#00ff41', anchor='w').pack(fill='x', pady=(10,4))
        
        for feature in self.suspect_features:
            tk.Label(info_frame, text=f"• {feature}", font=('Helvetica', 12),
                    bg='#2d3748', fg='#7d8590', anchor='w').pack(fill='x', pady=2)
        
        self.root.after(display_time, self._face_recognition_quiz)
    
    def _face_recognition_quiz(self):
        """Quiz on suspect details."""
        self.clear_window()
        
        self._show_header("FACE RECOGNITION", 3)
        
        tk.Label(self.root, text="Identify the suspect:",
                font=('Helvetica', 14), bg='#0a0e1a', fg='#7d8590').pack(pady=20)
        
        # Create multiple choice with correct answer and decoys
        choices = [self.suspect_name]
        first_names = ['ALEX', 'BLAKE', 'CASEY', 'DREW', 'ELLIS']
        last_names = ['ANDERSON', 'BROOKS', 'CARTER', 'DAVIS', 'EVANS']
        
        while len(choices) < 4:
            fake_name = f"{random.choice(first_names)} {random.choice(last_names)}"
            if fake_name not in choices:
                choices.append(fake_name)
        
        random.shuffle(choices)
        
        for choice in choices:
            btn = tk.Button(
                self.root,
                text=choice,
                font=('Helvetica', 14, 'bold'),
                bg='#2d3748',
                fg='#00ff41',
                command=lambda c=choice: self._check_face_answer(c),
                cursor='hand2',
                relief='flat',
                pady=12,
                padx=35
            )
            btn.pack(pady=10)
    
    def _check_face_answer(self, choice):
        """Check face recognition answer."""
        if choice == self.suspect_name:
            self.score += self.level * 10
            self.level += 1
            self.show_result(True, f"Correct! {self.suspect_name}")
            self.root.after(2000, self.face_recognition_round)
        else:
            self.show_result(False, f"Incorrect\nCorrect: {self.suspect_name}")
            self.end_game('face_recognition')
    
    # ========== M4: SAFE COMBINATIONS ==========
    
    def start_safe_combinations(self):
        """Start safe combination memorization training."""
        self.current_game = 'safe_combinations'
        self.score = 0
        self.level = 1
        self.safe_combination_round()
    
    def safe_combination_round(self):
        """Display safe combination."""
        self.clear_window()
        
        # Generate combination based on level
        combo_length = min(4 + self.level, 12)
        self.combination = '-'.join([''.join(random.choices(string.digits, k=2)) 
                                     for _ in range(combo_length // 2)])
        
        display_time = max(3000, 6000 - (self.level * 250))
        
        self._show_header("SAFE COMBINATIONS", 4)
        
        tk.Label(self.root, text="Memorize the combination",
                font=('Helvetica', 12), bg='#0a0e1a', fg='#7d8590', pady=10).pack()
        
        safe_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        safe_frame.pack(pady=30)
        
        tk.Label(safe_frame, text=self.combination, font=('Courier', 40, 'bold'),
                bg='#1a1f2e', fg='#00ff41', padx=50, pady=50).pack()
        
        self.root.after(display_time, lambda: self._get_text_input(
            "Enter the combination:",
            self.combination,
            self.safe_combination_round,
            'safe_combinations'
        ))
    
    # ========== M5: SURVEILLANCE DETAILS ==========
    
    def start_surveillance(self):
        """Start surveillance detail observation training."""
        self.current_game = 'surveillance_details'
        self.score = 0
        self.level = 1
        self.surveillance_round()
    
    def surveillance_round(self):
        """Display surveillance scene."""
        self.clear_window()
        
        # Generate scene details
        num_items = min(5 + self.level, 12)
        items = ['📱', '💼', '🔑', '📄', '💻', '🎒', '☕', '📚', '🕶️', '⌚', '🔦', '📷']
        self.scene_items = random.sample(items, num_items)
        self.missing_item = random.choice(self.scene_items)
        
        display_time = max(4000, 7000 - (self.level * 250))
        
        self._show_header("SURVEILLANCE DETAILS", 5)
        
        tk.Label(self.root, text="Observe all items in the scene",
                font=('Helvetica', 12), bg='#0a0e1a', fg='#7d8590', pady=10).pack()
        
        scene_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        scene_frame.pack(pady=20, padx=50)
        
        items_text = '  '.join(self.scene_items)
        tk.Label(scene_frame, text=items_text, font=('Arial', 28),
                bg='#1a1f2e', fg='#00ff41', padx=30, pady=30, wraplength=700).pack()
        
        self.root.after(display_time, self._surveillance_quiz)
    
    def _surveillance_quiz(self):
        """Quiz on missing item."""
        self.clear_window()
        
        remaining = [item for item in self.scene_items if item != self.missing_item]
        random.shuffle(remaining)
        
        self._show_header("SURVEILLANCE DETAILS", 5)
        
        tk.Label(self.root, text="Which item was removed?",
                font=('Helvetica', 14), bg='#0a0e1a', fg='#7d8590').pack(pady=15)
        
        scene_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        scene_frame.pack(pady=15, padx=50)
        
        items_text = '  '.join(remaining)
        tk.Label(scene_frame, text=items_text, font=('Arial', 24),
                bg='#1a1f2e', fg='#7d8590', padx=30, pady=20, wraplength=700).pack()
        
        choices = [self.missing_item] + random.sample([i for i in self.scene_items if i != self.missing_item], 
                                                       min(3, len(self.scene_items) - 1))
        random.shuffle(choices)
        
        btn_frame = tk.Frame(self.root, bg='#0a0e1a')
        btn_frame.pack(pady=20)
        
        for choice in choices:
            btn = tk.Button(
                btn_frame,
                text=choice,
                font=('Arial', 24),
                bg='#2d3748',
                fg='#00ff41',
                command=lambda c=choice: self._check_surveillance_answer(c),
                cursor='hand2',
                relief='flat',
                padx=15,
                pady=8
            )
            btn.pack(side='left', padx=8)
    
    def _check_surveillance_answer(self, choice):
        """Check surveillance answer."""
        if choice == self.missing_item:
            self.score += self.level * 10
            self.level += 1
            self.show_result(True, f"Correct! Missing: {self.missing_item}")
            self.root.after(2000, self.surveillance_round)
        else:
            self.show_result(False, f"Incorrect\nMissing: {self.missing_item}")
            self.end_game('surveillance_details')
    
    # ========== M6: MAP MEMORIZATION ==========
    
    def start_map_memory(self):
        """Start tactical map memorization training."""
        self.current_game = 'map_memorization'
        self.score = 0
        self.level = 1
        self.map_memory_round()
    
    def map_memory_round(self):
        """Display tactical waypoints."""
        self.clear_window()
        
        # Generate waypoint sequence
        num_waypoints = min(3 + self.level, 10)
        directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NE', 'NW', 'SE', 'SW']
        self.waypoints = [random.choice(directions) for _ in range(num_waypoints)]
        
        display_time = max(3000, 6000 - (self.level * 250))
        
        self._show_header("MAP MEMORIZATION", 6)
        
        tk.Label(self.root, text="Memorize the route sequence",
                font=('Helvetica', 12), bg='#0a0e1a', fg='#7d8590', pady=10).pack()
        
        map_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        map_frame.pack(pady=20)
        
        tk.Label(map_frame, text="Route", font=('Helvetica', 14, 'bold'),
                bg='#1a1f2e', fg='#00ff41', pady=8).pack()
        
        for i, waypoint in enumerate(self.waypoints, 1):
            tk.Label(map_frame, text=f"{i}. {waypoint}", font=('Helvetica', 16, 'bold'),
                    bg='#1a1f2e', fg='#00ff41', pady=4).pack()
        
        tk.Label(map_frame, text="", pady=5).pack()
        
        self.root.after(display_time, lambda: self._get_multiline_input(
            "Enter the route (one direction per line):",
            self.waypoints,
            self.map_memory_round,
            'map_memorization'
        ))
    
    # ========== HELPER FUNCTIONS ==========
    
    def _show_header(self, mission_name, mission_num):
        """Display mission header."""
        tk.Label(self.root, text=f"{mission_name} - Level {self.level}",
                font=('Helvetica', 20, 'bold'), bg='#0a0e1a', fg='#00ff41').pack(pady=20)
        
        tk.Label(self.root, text=f"Score: {self.score}", font=('Helvetica', 13),
                bg='#0a0e1a', fg='#7d8590').pack()
    
    def _get_text_input(self, prompt, correct_answer, next_round, game_type):
        """Get single-line text input."""
        self.clear_window()
        
        self._show_header(game_type.replace('_', ' ').upper(), 
                         list(self.stats.keys()).index(game_type) + 1)
        
        tk.Label(self.root, text=prompt, font=('Helvetica', 14),
                bg='#0a0e1a', fg='#7d8590').pack(pady=25)
        
        input_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        input_frame.pack(pady=15)
        
        entry = tk.Entry(input_frame, font=('Courier', 20, 'bold'),
                        bg='#2d3748', fg='#00ff41', insertbackground='#00ff41',
                        justify='center', width=28)
        entry.pack(pady=15, padx=15)
        entry.focus()
        
        def check():
            if entry.get().strip().upper() == correct_answer:
                self.score += self.level * 10
                self.level += 1
                self.show_result(True, f"Correct!")
                self.root.after(2000, next_round)
            else:
                self.show_result(False, f"Incorrect\nCorrect answer: {correct_answer}")
                self.end_game(game_type)
        
        tk.Button(self.root, text="Submit", font=('Helvetica', 13, 'bold'),
                 bg='#2d3748', fg='#00ff41', command=check,
                 cursor='hand2', relief='flat', pady=12, padx=40).pack(pady=20)
        
        entry.bind('<Return>', lambda e: check())
    
    def _get_multiline_input(self, prompt, correct_list, next_round, game_type):
        """Get multi-line text input."""
        self.clear_window()
        
        self._show_header(game_type.replace('_', ' ').upper(),
                         list(self.stats.keys()).index(game_type) + 1)
        
        tk.Label(self.root, text=prompt, font=('Helvetica', 14),
                bg='#0a0e1a', fg='#7d8590').pack(pady=20)
        
        text_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        text_frame.pack(pady=15)
        
        text = tk.Text(text_frame, font=('Courier', 15, 'bold'),
                      bg='#2d3748', fg='#00ff41', insertbackground='#00ff41',
                      width=32, height=len(correct_list) + 2)
        text.pack(pady=12, padx=12)
        text.focus()
        
        def check():
            user_input = [line.strip().upper() for line in text.get('1.0', 'end').strip().split('\n')]
            if user_input == correct_list:
                self.score += self.level * 10
                self.level += 1
                self.show_result(True, "All correct!")
                self.root.after(2000, next_round)
            else:
                correct_str = '\n'.join(correct_list)
                self.show_result(False, f"Incorrect\n\nCorrect:\n{correct_str}")
                self.end_game(game_type)
        
        tk.Button(self.root, text="Submit", font=('Helvetica', 13, 'bold'),
                 bg='#2d3748', fg='#00ff41', command=check,
                 cursor='hand2', relief='flat', pady=12, padx=40).pack(pady=15)
    
    def show_result(self, is_correct, message):
        """Show result overlay."""
        overlay = tk.Frame(self.root, bg='#0a0e1a')
        overlay.place(relx=0.5, rely=0.5, anchor='center')
        
        result_frame = tk.Frame(overlay, bg='#1a1f2e', relief='solid', bd=3)
        result_frame.pack(padx=40, pady=40)
        
        status = "✓ Success" if is_correct else "✗ Incorrect"
        color = '#00ff41' if is_correct else '#ff6b6b'
        
        tk.Label(result_frame, text=status, font=('Helvetica', 18, 'bold'),
                bg='#1a1f2e', fg=color, padx=35, pady=18).pack()
        
        tk.Label(result_frame, text=message, font=('Helvetica', 13),
                bg='#1a1f2e', fg='#7d8590', padx=35, pady=18, justify='center').pack()
    
    def end_game(self, game_type):
        """End current mission."""
        self.stats[game_type]['played'] += 1
        self.stats[game_type]['total_score'] += self.score
        if self.score > self.stats[game_type]['best_score']:
            self.stats[game_type]['best_score'] = self.score
        self.save_stats()
        
        self.root.after(3000, self.show_final_score)
    
    def show_final_score(self):
        """Show mission debrief."""
        self.clear_window()
        
        tk.Label(self.root, text="Session Complete", font=('Helvetica', 28, 'bold'),
                bg='#0a0e1a', fg='#00ff41').pack(pady=30)
        
        score_frame = tk.Frame(self.root, bg='#1a1f2e', relief='solid', bd=2)
        score_frame.pack(pady=15)
        
        tk.Label(score_frame, text=f"Final Score: {self.score}\nLevel Reached: {self.level}",
                font=('Helvetica', 22, 'bold'), bg='#1a1f2e', fg='#00ff41',
                padx=50, pady=30).pack()
        
        if self.current_game:
            best = self.stats[self.current_game]['best_score']
            tk.Label(self.root, text=f"Personal Best: {best}", font=('Helvetica', 15),
                    bg='#0a0e1a', fg='#7d8590').pack(pady=10)
        
        btn_frame = tk.Frame(self.root, bg='#0a0e1a')
        btn_frame.pack(pady=25)
        
        tk.Button(btn_frame, text="Try Again", font=('Helvetica', 13, 'bold'),
                 bg='#2d3748', fg='#00ff41', command=self.restart_current_game,
                 cursor='hand2', relief='flat', pady=12, padx=30).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Main Menu", font=('Helvetica', 13, 'bold'),
                 bg='#2d3748', fg='#7d8590', command=self.create_main_menu,
                 cursor='hand2', relief='flat', pady=12, padx=30).pack(side='left', padx=10)
    
    def restart_current_game(self):
        """Restart current mission."""
        game_map = {
            'document_recall': self.start_document_recall,
            'license_plates': self.start_license_plates,
            'face_recognition': self.start_face_recognition,
            'safe_combinations': self.start_safe_combinations,
            'surveillance_details': self.start_surveillance,
            'map_memorization': self.start_map_memory
        }
        if self.current_game in game_map:
            game_map[self.current_game]()


def main():
    """Main entry point."""
    root = tk.Tk()
    app = OperationalMemoryTraining(root)
    root.mainloop()


if __name__ == "__main__":
    main()
