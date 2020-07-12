class Translator:

    __level_fields = ['sustainability', 'rain_regime', 'investment']

    @classmethod
    def translate_knowledge(cls, knowledge: dict) -> dict:
        """ Translate from spanish to english. """
        translated = dict()
        for key, value in knowledge.items():
            if key in cls.__level_fields:
                translated[key] = cls.__level_translation()[value.lower()]
            elif key == 'exploitation':
                translated[key] = cls.__exploitation_translation()[value.lower()]
            elif key == 'last_crop':
                translated[key] = cls.__crop_translation()[value.lower()]
            elif key == 'month':
                translated[key] = cls.__months().index(value.lower()) + 1
        return translated

    @classmethod
    def translate_result(cls, result: str) -> str:
        """ Translate result from english to spanish. """
        for key, value in cls.__crop_translation().items():
            if value == result:
                return key.capitalize()

    @classmethod
    def __level_translation(cls):
        return {
            'alto': 'high',
            'alta': 'high',
            'medio': 'mid',
            'media': 'mid',
            'bajo': 'low',
            'baja': 'low'
        }

    @classmethod
    def __exploitation_translation(cls):
        return {
            'ganadería': 'cattle',
            'ganderia': 'cattle',
            'agricultura': 'agriculture',
            'mixta': 'mixed'
        }

    @classmethod
    def __crop_translation(cls):
        return {
            'soja': 'soy',
            'avena': 'oats',
            'sorgo': 'sorghum',
            'trigo': 'wheat',
            'maíz': 'corn',
            'maiz': 'corn',
            'cebada': 'barley',
            'girasol': 'sunflower'
        }

    @classmethod
    def __months(cls):
        return [
            'enero',
            'febrero',
            'marzo',
            'abril',
            'mayo',
            'junio',
            'julio',
            'agosto',
            'septiembre',
            'octubre',
            'noviembre',
            'diciembre'
        ]
