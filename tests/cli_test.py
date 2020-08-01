import hypergan as hg
import hyperchamber as hc
import tensorflow as tf
import os
from hypergan.gan_component import ValidationException

from inputs.image_loader_test import fixture_path
from mocks import MockDiscriminator, mock_gan
import shutil

from hypergan.multi_component import MultiComponent
from hypergan.losses.supervised_loss import SupervisedLoss

def gan_fn(config, inputs, distribution_strategy=None, session=None, reuse=False, graph=None):
    gan = hg.GAN(config=config, inputs=inputs, debug=args.debug, device=args.device, distribution_strategy=distribution_strategy, session=session, reuse=reuse, graph=graph)
    gan.args = args
    gan.x_width = width
    gan.x_height = height
    gan.x_channels = channels
    gan.name = config_name
    return gan

class CliTest(tf.test.TestCase):
    def test_cli(self):
        with self.test_session():
            gan = mock_gan()
            args = {
            }
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            self.assertEqual(cli.gan, gan)

    def test_run(self):
        with self.test_session():
            gan = mock_gan()
            args = hc.Config({"size": "1"})
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            cli.run()
            self.assertEqual(cli.gan, gan)

    def test_step(self):
        with self.test_session():
            gan = mock_gan()
            args = hc.Config({"size": "1", "steps": 1, "method": "train", "save_every": -1})
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            cli.step()
            self.assertEqual(cli.gan, gan)

    def test_sample(self):
        with self.test_session():
            gan = mock_gan()
            args = hc.Config({"size": "1", "steps": 1, "method": "train", "save_every": -1})
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            cli.sample('/tmp/test-sample.png')
            self.assertEqual(cli.gan, gan)


    def test_train(self):
        with self.test_session():
            gan = mock_gan()
            args = hc.Config({"size": "1", "steps": 1, "method": "train", "save_every": -1})
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            cli.train()
            self.assertEqual(cli.gan, gan)

    def test_adds_supervised_loss(self):
        with self.test_session():
            gan = mock_gan(y=2)
            args = hc.Config({"size": "1", "steps": 1, "method": "train", "save_every": -1, "classloss": True})
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            cli.add_supervised_loss()
            self.assertEqual(type(cli.gan.loss), MultiComponent)
            self.assertEqual(type(cli.gan.loss.components[0]), SupervisedLoss)

    def test_new(self):
        with self.test_session():
            try: 
                os.remove('test.json')
            except Exception:
                pass
            gan = mock_gan()
            args = hc.Config({"size": "1", "steps": 1, "method": "train", "directory": "test"})
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            cli.new()
            self.assertTrue(os.path.isfile('test.json'))

    def test_safe_new(self):
        with self.test_session():
            try: 
                os.remove('test.json')
            except Exception:
                pass
            gan = mock_gan()
            args = hc.Config({"size": "1", "steps": 1, "method": "train", "directory": "test"})
            cli = hg.CLI(gan_fn=gan_fn, args=args)
            cli.new()
            with self.assertRaises(ValidationException):
                cli.new()


if __name__ == "__main__":
    tf.test.main()
