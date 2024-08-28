import code_for_test_2 as code
import unittest


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.Usein = code.Runner('Усейн', speed=10)
        self.Andrey = code.Runner('Андрей', speed=9)
        self.Nik = code.Runner('Ник', speed=3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_run_1(self):
        test_tournament = code.Tournament(90,
                                          self.Usein, self.Nik)
        res = test_tournament.start()
        self.all_results['Усейн и Ник'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Nik)

    def test_run_2(self):
        test_tournament = code.Tournament(90,
                                          self.Andrey, self.Nik)
        res = test_tournament.start()
        self.all_results['Андрей и Ник'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Nik)

    def test_run_3(self):
        test_tournament = code.Tournament(90,
                                          self.Usein, self.Andrey, self.Nik)
        res = test_tournament.start()
        self.all_results['Усейн, Андрей и Ник'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Nik)

    def test_run_4(self):
        """
        Если дистанция меньше или равна меньшей скорости в списке, то бегун с меньшей
        скоростью может прийти первым, если начинает первым.
        Для исправления ошибки, ввел 2 дандер метода в класс Runner и отсортировал
        список бегунов по убиванию скорости
        :return:
        """
        test_tournament = code.Tournament(9,
                                          self.Andrey, self.Usein)
        res = test_tournament.start()
        self.all_results['Андрей - Усейн'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Andrey)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(key)
            for i in cls.all_results[key]:
                print(f'{cls.all_results[key][i]} - {i}')
            print()


if __name__ == '__main__':
    unittest.main()
