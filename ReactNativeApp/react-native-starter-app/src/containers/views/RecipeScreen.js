// Consts and Libs
import {AppColors, AppSizes, AppStyles} from '@theme/';
// Components
import {Button, Spacer} from '@ui/';
import React, {Component} from 'react';
import {Image, StyleSheet, Text, View} from 'react-native';
import {Actions} from 'react-native-router-flux';

/* Styles ====================================================================
 */
const styles = StyleSheet.create({
  background: {
    backgroundColor: AppColors.brand.primary,
    height: AppSizes.screen.height,
    width: AppSizes.screen.width,
  },
  logo: {
    width: AppSizes.screen.width * 0.85,
    resizeMode: 'contain',
  },
  whiteText: {
    color: '#FFF',
  },
});



/* Component
 * ==================================================================== */
class RecipeScreen extends Component {
  static componentName = 'StartScreen';

  render = () =>
      (<View style =
            {[AppStyles.containerCentered, AppStyles.container,
              styles.background]}>
       <Text style = {styles.whiteText} onPress =
            {() => Actions.detailedRecipeScreen()}>Welcome to the Anya Cooking
           Asistant!</Text>
    </View>)
}

/* Export Component
 * ==================================================================== */
export default RecipeScreen;