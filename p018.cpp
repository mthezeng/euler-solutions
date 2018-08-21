/*
 * A* Algorithm to find the maximum-sum path in a triangle of cells
 * Problems 18 and 67 on Project Euler
 * Author: Teemu
 *
 * Usage:
 * $ g++ p018.cpp -o p018
 * $ .\p018 n file.txt
 * where n is the number of rows in the triangle and file.txt is the source file
 * such as https://projecteuler.net/project/resources/p067_triangle.txt
 */

#include <iostream>
#include <fstream>
#include <queue>
#include <vector>


class Node {
  public:
    int row;
    int col;
    int score;
    int moves;
    int weight;
    Node(int r, int c, int s, int m, int w) {
      Node::row = r;
      Node::col = c;
      Node::score = s;
      Node::moves = m;
      Node::weight = w;
    }
};


// The Heuristic
struct CompareNodes {
  bool operator()(const Node& a, const Node& b) const {
    return (a.score - a.weight*a.moves) < (b.score - b.weight*b.moves);
  }
};


class TrianglePath {
  private:
    int solution;
    int count;
    double INV_SPEED;
  public:
    double WEIGHT;
    TrianglePath(char* s, char* f);
    int get_solution();
    int cells_visited();
};


TrianglePath::TrianglePath(char* s, char* f) {
  char* end;
  int size = std::strtol(s, &end, 10);
  int triangle[size][size];

  std::fstream datafile(f, std::ios_base::in);

  // construct the triangle as a 2D array
  int row = 0;
  int col = 0;
  int val;
  int sum = 0;
  while (datafile >> val) {
    triangle[row][col] = val;
    sum += val;
    if (row == col) {
      row++;
      col = 0;
    } else {
      col++;
    }
  }


  // change this to modify the thorough-ness of the A* algorithm
  // Suggested range: 0 to 2
  // Smaller values make algorithm more Greedy-like
  // Larger values make the algorithm visit more cells
  double INV_SPEED = 1.33;
  TrianglePath::WEIGHT = INV_SPEED * (double) sum / (0.5 * size * size);


  /* The A*-algorithm */
  std::priority_queue<Node, std::vector<Node>, CompareNodes> pq;

  Node start(0, 0, triangle[0][0], 0, TrianglePath::WEIGHT);
  pq.push(start);

  Node current = pq.top();
  pq.pop();

  TrianglePath::count = 0;

  while (current.row < size - 1) {
    TrianglePath::count++;

    // terminate if algorithm takes too long to find solution
    if (TrianglePath::count == 10000000) {
      std::cout << "Stopped at row " << current.row << std::endl;
      std::cout << current.score << std::endl;
    }

    int row1 = current.row + 1;
    int col1 = current.col;
    int col2 = current.col + 1;
    Node next1(row1, col1, current.score+triangle[row1][col1], current.moves+1, TrianglePath::WEIGHT);
    Node next2(row1, col2, current.score+triangle[row1][col2], current.moves+1, TrianglePath::WEIGHT);
    pq.push(next1);
    pq.push(next2);

    current = pq.top();
    pq.pop();
  };

  TrianglePath::solution = current.score;
};


int TrianglePath::get_solution() {
  return TrianglePath::solution;
};


int TrianglePath::cells_visited() {
  return TrianglePath::count;
};


int main(int argc, char* argv[]) {

  TrianglePath tp(argv[1], argv[2]);
  std::cout << "Solution: " << tp.get_solution() << std::endl;
  std::cout << "Number of cells visitited: " << tp.cells_visited() << std::endl;

  return 0;
};
