# Run all tests
# Each test module should define a run() function

testmodules = [
    'hackystone_app.utils.test_utils',
    'hackystone_app.algorithms.test_algorithms',
    'hackystone_app.models.test_measurement'
]

for t in testmodules:
    try:
        mod = __import__(t, globals(), locals(), ['run'])
        mod.run()
    except (ImportError, AttributeError) as e:
        print("Testmodule %s failed" % (t))
        print(e)