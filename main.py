def move_files_by_suffix(source_folder, target_folder, suffixes, recursive=False):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist!")
        return

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Log file to track the operations
    log_file = os.path.join(target_folder, "file_move_log.txt")
    
    def move_file(source_path, target_path, filename):
        if os.path.exists(target_path):
            # Handle filename conflicts by renaming (appending a timestamp)
            base, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            target_path = os.path.join(target_folder, f"{base}_{timestamp}{ext}")
        
        shutil.move(source_path, target_path)
        log_entry = f"Moved: {source_path} -> {target_path}\n"
        with open(log_file, 'a') as log:
            log.write(log_entry)
        print(log_entry.strip())

    if recursive:
        # If recursive, traverse all subdirectories
        for root, dirs, files in os.walk(source_folder):
            for filename in files:
                if filename.endswith(suffixes):
                    source_path = os.path.join(root, filename)
                    target_path = os.path.join(target_folder, filename)
                    move_file(source_path, target_path, filename)
    else:
        # Only process the current directory (non-recursive)
        for filename in os.listdir(source_folder):
            if filename.endswith(suffixes):
                source_path = os.path.join(source_folder, filename)
                target_path = os.path.join(target_folder, filename)
                move_file(source_path, target_path, filename)

    print(f"Operation completed. See log file at {log_file}")
