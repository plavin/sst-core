import sst

obj = sst.Component("example_component_name", "{{ELEMENT_NAME}}.{{COMPONENT_NAME}}")
obj.addParams(
    {
        "printFrequency" : "5",
        "repeats" : "15",
    }
)

