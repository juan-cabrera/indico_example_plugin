# indico_example_plugin

Example plugin for [indico](https://getindico.io/) 

Created following instructions on the
[indico documentation](https://docs.getindico.io/en/stable/plugins/getting_started/)

## Example installation

Clone the project and install

    git clone https://github.com/juan-cabrera/indico_example_plugin.git
    cd indico_example_plugin
    pip install .

Add the plugin in the indico configuration file

    PLUGINS = { 'indico_example',
                'plugin1',
                'plugin2'
              }

Update plugin DB

    indico db --all-plugins upgrade

Restart indico

    systemctl restat indico-celery
