import param
import panel as pn
pn.extension()
class ActionExample(param.Parameterized):
    """
    Demonstrates how to use param.Action to trigger an update.
    """
    number = param.Number(default=0)
    action = param.Action(lambda x: x.param.trigger('action'), label='Click here!')

    @param.depends('action')
    def get_number(self):
        return self.number

action_example = ActionExample(name='')

pn.Row('# param.Action Example',
    pn.Column(   pn.panel(action_example.param),
            'Click the button to trigger an update in the output.'),
        pn.WidgetBox(action_example.get_number, width=300)).servable()