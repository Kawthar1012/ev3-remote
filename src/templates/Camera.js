import React, { useState } from "react";
import { StyleSheet, Text, View } from "react-native";
import { Button, Image } from "react-native";

const Camera = ({navigation}) => {
    return (
    <View style={styles.container}>
       <Image
        source={{uri:"http://localhost:5000/video_feed" }} 
        style = {{ width: 500, height: 500 }}
       />
       <View>
       <Button title='Go back' onPress={() => navigation.navigate('Home')}/>
        </View>
    </View>
     );
    };export default Camera;

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center'
    }
  })
