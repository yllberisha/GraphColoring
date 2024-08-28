# import json

# def generate_sudoku_paths():
#     paths = []
#     node_id = 0

#     # Generate paths for a 4x4 Sudoku-like structure
#     for row in range(4):
#         for col in range(4):
#             current_node = row * 4 + col
#             for i in range(4):
#                 if i != col:
#                     paths.append({"id": node_id, "from": current_node, "to": row * 4 + i})
#                     node_id += 1
#                 if i != row:
#                     paths.append({"id": node_id, "from": current_node, "to": i * 4 + col})
#                     node_id += 1

#     # Save the paths to a JSON file
#     with open('sudoku_paths.json', 'w') as file:
#         json.dump({"paths": paths}, file, indent=4)

# if __name__ == "__main__":
#     generate_sudoku_paths()





# generate_sudoku_paths for 4x4
# import json

# def generate_sudoku_paths():
#     paths = []
#     node_id = 0

#     # Generate paths for a 4x4 Sudoku-like structure
#     for row in range(4):
#         for col in range(4):
#             current_node = row * 4 + col
#             for i in range(4):
#                 if i != col:
#                     paths.append({"id": node_id, "from": current_node, "to": row * 4 + i})
#                     node_id += 1
#                 if i != row:
#                     paths.append({"id": node_id, "from": current_node, "to": i * 4 + col})
#                     node_id += 1

#             # Add square connections
#             square_row = row // 2
#             square_col = col // 2
#             for r in range(square_row * 2, (square_row + 1) * 2):
#                 for c in range(square_col * 2, (square_col + 1) * 2):
#                     if r != row and c != col:
#                         paths.append({"id": node_id, "from": current_node, "to": r * 4 + c})
#                         node_id += 1

#     # Save the paths to a JSON file
#     with open('sudoku_paths.json', 'w') as file:
#         json.dump({"paths": paths}, file, indent=4)

# if __name__ == "__main__":
#     generate_sudoku_paths()


import json

# Create an empty list to store the paths
paths = []

# Define the size of the Sudoku grid (9x9)
grid_size = 9

# Function to get the 3x3 subgrid index for a given cell
def get_subgrid_index(row, col):
    return (row // 3) * 3 + (col // 3)

# Generate paths for all nodes in the Sudoku grid
for row in range(grid_size):
    for col in range(grid_size):
        for target_row in range(grid_size):
            # Add paths for the same row
            if row != target_row:
                paths.append({"id": len(paths), "from": row * grid_size + col, "to": target_row * grid_size + col})
        for target_col in range(grid_size):
            # Add paths for the same column
            if col != target_col:
                paths.append({"id": len(paths), "from": row * grid_size + col, "to": row * grid_size + target_col})
        subgrid_index = get_subgrid_index(row, col)
        for target_row in range(subgrid_index // 3 * 3, subgrid_index // 3 * 3 + 3):
            for target_col in range(subgrid_index % 3 * 3, subgrid_index % 3 * 3 + 3):
                # Add paths for nodes within the same 3x3 subgrid
                if row != target_row or col != target_col:
                    paths.append({"id": len(paths), "from": row * grid_size + col, "to": target_row * grid_size + target_col})

# Create a dictionary with the paths
data = {"paths": paths}

# Remove duplicate paths (e.g., from 0 to 1 and from 1 to 0)
unique_paths = [dict(t) for t in {tuple(d.items()) for d in data["paths"]}]
data["paths"] = unique_paths

# Write the JSON data to a text file
with open("sudoku_paths.json", "w") as file:
    json.dump(data, file, indent=2)

print("Paths generated and saved to 'sudoku_paths.json'.")
