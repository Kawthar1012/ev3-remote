import { useNavigation } from "@react-navigation/native";
import React from "react";
import { StyleSheet, Text, View } from 'react-native';

import Header from './Header';
import Boxes from './Boxes';
import { Button } from 'react-native-web';


const Home = ({navigation}) => {
    return(
      <View style={styles.container}>
        <Header />
        <Boxes navigation={navigation}/>
      </View>
    );
};

export default Home;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center'
  }
})