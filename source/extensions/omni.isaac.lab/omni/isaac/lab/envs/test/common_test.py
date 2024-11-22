
import unittest
from omni.isaac.lab.utils import configclass
from typing import Literal

@configclass
class ViewerCfg:
    eye: tuple[float, float, float] = (7.5, 7.5, 7.5)
    lookat: tuple[float, float, float] = (0.0, 0.0, 0.0)
    cam_prim_path: str = "/OmniverseKit_Persp"
    resolution: tuple[int, int] = (1280, 720)
    origin_type: Literal["world", "env", "asset_root"] = "world"
    env_index: int = 0
    asset_name: str | None = None

class TestViewerCfg(unittest.TestCase):

    def test_default_initialization(self):
        """Test ViewerCfg initializes with default values."""
        cfg = ViewerCfg()
        self.assertEqual(cfg.eye, (7.5, 7.5, 7.5))
        self.assertEqual(cfg.lookat, (0.0, 0.0, 0.0))
        self.assertEqual(cfg.cam_prim_path, "/OmniverseKit_Persp")
        self.assertEqual(cfg.resolution, (1280, 720))
        self.assertEqual(cfg.origin_type, "world")
        self.assertEqual(cfg.env_index, 0)
        self.assertIsNone(cfg.asset_name)


if __name__ == '__main__':
    unittest.main()