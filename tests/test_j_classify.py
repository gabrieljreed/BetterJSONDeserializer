"""Unit tests for the j_classify package."""

import json
import unittest
import tempfile

import j_classify


class TestJObject(unittest.TestCase):
    """Test the j_object package."""

    def setUp(self) -> None:
        """Set up the test case."""
        # Create a temp folder to store the test files
        self.temp_folder = tempfile.TemporaryDirectory()
        return super().setUp()

    def tearDown(self) -> None:
        """Tear down the test case."""
        # Delete the temp folder
        self.temp_folder.cleanup()
        return super().tearDown()

    def test_load_j_object(self) -> None:
        """Test the load_j_object function."""
        pass

    def test_list_all_j_objects(self) -> None:
        """Test the list_all_j_objects function."""
        pass

    def test_j_object(self) -> None:
        """Test the j_object class."""
        class test_class_1(j_classify.j_object):
            def __init__(self) -> None:
                super().__init__()
                self.name = "test_class_1"
                self.number = 1
                self.boolean = True
                self.children: list = []

        class test_class_2(j_classify.j_object):
            def __init__(self) -> None:
                super().__init__()
                self.name = "test_class_2"
                self.number = 2
                self.boolean = False
                self.children: list = []

        class test_class_3(j_classify.j_object):
            def __init__(self) -> None:
                super().__init__()
                self.name = "test_class_3"
                self.number = 3
                self.boolean = True

        obj_1 = test_class_1()
        obj_2 = test_class_2()
        obj_3 = test_class_3()

        self.assertTrue(isinstance(obj_1, j_classify.j_object), "obj_1 is not a j_object")
        self.assertTrue(isinstance(obj_2, j_classify.j_object), "obj_2 is not a j_object")
        self.assertTrue(isinstance(obj_3, j_classify.j_object), "obj_3 is not a j_object")

    def test_j_object_encoder(self) -> None:
        """Test the j_object_encoder class."""
        class test_class_1(j_classify.j_object):
            def __init__(self) -> None:
                super().__init__()
                self.name = "test_class_1"
                self.number = 1
                self.boolean = True
                self.children: list = []

        class test_class_2(j_classify.j_object):
            def __init__(self) -> None:
                super().__init__()
                self.name = "test_class_2"
                self.number = 2
                self.boolean = False
                self.children: list = []

        class test_class_3(j_classify.j_object):
            def __init__(self) -> None:
                super().__init__()
                self.name = "test_class_3"
                self.number = 3
                self.boolean = True

        obj_1 = test_class_1()
        obj_2 = test_class_2()
        obj_3 = test_class_3()

        self.assertTrue(isinstance(obj_1, j_classify.j_object), "obj_1 is not a j_object")
        self.assertTrue(isinstance(obj_2, j_classify.j_object), "obj_2 is not a j_object")
        self.assertTrue(isinstance(obj_3, j_classify.j_object), "obj_3 is not a j_object")

        obj_1.children.append(obj_2)
        obj_2.children.append(obj_3)

        obj_data = json.dumps(obj_1, cls=j_classify.j_object_encoder, indent=4)
        self.assertTrue(isinstance(obj_data, str), "obj_data is not a string")
        print(obj_data)
