from readability.exceptions import ReadabilityException


class Result:
    def __init__(self, score, grade_level):
        self.score = score
        self.grade_level = grade_level

    def __str__(self):
        return "score: {}, grade_level: '{}'". \
            format(self.score, self.grade_level)


class WienerSachtextformel:
    def __init__(self, stats, min_words=100, language='de'):
        self._stats = stats
        if stats.num_words < min_words:
            raise ReadabilityException('{} words required.'.format(min_words))

    def score(self):
        score = self._score()
        return Result(
            score=score,
            grade_level=self._grade_level(score)
        )

    def _score(self):
        stats = self._stats
        return (0.1935 * (stats.num_poly_syllable_words / stats.num_words)*100) + (0.1672 * stats.num_words) + \
               (0.1297 * (stats.num_six_letter_words / stats.num_words)*100) - (0.0327 * (stats.num_mono_syllable_words / stats.num_words)*100) - 15.59

    def _ease(self, score):
        if score >= 4 and score <= 5:
            return 'very_easy'
        elif score >=6 and score <=7:
            return 'easy'
        elif score >=8 and score <=10:
            return 'average'
        elif score >=11 and score <=12:
            return 'difficult'
        else:
            return 'very_difficult'

    def _grade_level(self, score):
        if score >= 4 and score <= 5:
            return ['4th-5th grade']
        elif score >=6 and score <=7:
            return ['6th-7th grade']
        elif score >=8 and score <=10:
            return ['8th-10th grade']
        elif score >=11 and score <=12:
            return ['11th-12th grade']
        else:
            return ['college level and above']
