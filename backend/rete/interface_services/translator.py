class Translator:

    __level_fields = ['sustainability', 'rain_regime', 'investment']
    __key_translation = {
        'sustainability': 'Sustentabilidad',
        'rain_regime': 'Régimen de lluvia',
        'investment': 'Nivel de inversión',
        'exploitation': 'Tipo de explotación',
        'last_crop': 'Último cultivo',
        'month': 'Mes'
    }

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
    def translate_knowledge_return(cls, knowledge: dict) -> dict:
        translated = dict()
        for key, value in knowledge.items():
            if key in cls.__level_fields:
                translated[cls.__key_translation[key]] = cls.find_key(cls.__level_translation(), value).capitalize()
            elif key == 'exploitation':
                translated['Tipo de explotación'] = cls.find_key(cls.__exploitation_translation(), value).capitalize()
            elif key == 'last_crop':
                translated['Último cultivo'] = cls.find_key(cls.__crop_translation(), value).capitalize()
            elif key == 'month':
                translated['Mes'] = cls.__months()[value - 1].capitalize()
        return translated

    @classmethod
    def find_key(cls, dictionary: dict, value: str) -> str:
        for k, v in dictionary.items():
            if v == value: return k

    @classmethod
    def translate_result(cls, result: str) -> str:
        """ Translate result from english to spanish. """
        for key, value in cls.__crop_translation().items():
            if value.lower() == result.lower():
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
            'ganaderia': 'cattle',
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
