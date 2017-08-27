/**
 * App Navigation
 *
 * React Native Starter App
 * https://github.com/mcnamee/react-native-starter-app
 */
import React from 'react';
import { Actions, Scene, ActionConst } from 'react-native-router-flux';

// Consts and Libs
import { AppConfig } from '@constants/';

// Components
import Drawer from '@containers/ui/DrawerContainer';

// Scenes
import AppLaunch from '@containers/Launch/LaunchContainer';
import Placeholder from '@components/general/Placeholder';

import StartScreen from '@containers/views/StartScreen';
import RecipeScreen from '@containers/views/RecipeScreen';
import DetailedRecipeScreen from '@containers/views/DetailedRecipeScreen';
import TabsScenes from './tabs';

/* Routes ==================================================================== */
export default Actions.create(
  <Scene key={'root'} {...AppConfig.navbarProps}>
    <Scene
      hideNavBar
      key='splash'
      component={AppLaunch}
      analyticsDesc={'AppLaunch: Launching App'}
    />
    <Scene
      hideNavBar
      key='startScreen'
      component={StartScreen}
      analyticsDesc={'Welcome'}
      />
     <Scene
      key='recipeScreen'
      component={RecipeScreen}
      analyticsDesc={'Recipes'}
      />
      <Scene
      key='detailedRecipeScreen'
      component={DetailedRecipeScreen}
      analyticsDesc={'Recipes'}
      />
  </Scene>
);
