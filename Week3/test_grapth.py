import unittest
from graph import DirectedGraph

class TestGraph(unittest.TestCase):

    def setUp(self):

        self.my_graph = DirectedGraph("My Graph")

    def test_init(self):

        self.assertEqual(self.my_graph.name, "My Graph")
        self.assertEqual(self.my_graph.edges, {})

    def test_add_edge(self):

        self.my_graph.add_edge("Ivo", "Boqn")
        self.assertIn("Ivo", self.my_graph.edges.keys())
        self.assertIn("Boqn", self.my_graph.edges["Ivo"])

    def test_get_neighbors_for(self):

        self.my_graph.add_edge("Ivo", "Djihad")
        self.my_graph.add_edge("Ivo", "Ahmed")
        self.assertEqual(["Djihad", "Ahmed"], self.my_graph.get_neighbors_for("Ivo"))


    def test_str(self):

        self.my_graph.add_edge("Ivo", "Djihad")
        self.my_graph.add_edge("Ivo", "Ahmed")
        self.my_graph.__str__()

    def test_path_between(self):

        self.my_graph.add_edge("misho", 'pesho')
        self.my_graph.add_edge("pesho", 'mitko')
        self.my_graph.add_edge("mitko", 'stefcho')

        self.assertTrue(self.my_graph.path_between("misho", "stefcho"))



if __name__ == '__main__':
    unittest.main()

