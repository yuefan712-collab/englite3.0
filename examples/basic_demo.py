from englite import Converter

# Initialize the logic engine
engine = Converter(mode='native_26')

text = "The knight looked at the beautiful vision at night."
result = engine.translate(text)

print(result)
# Output: "ŧe NIIT luuk-ed at ŧe BYUU-ti-ful **VIZ-ion** at NIIT."
