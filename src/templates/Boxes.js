import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

const Boxes = ({ navigation }) => {
  return(
    <View style={styles.container}>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Button 
            title="Left" 
            onPress={() => navigation.navigate('Robot', {direction: 'left'})}
          />
        </View>
      </View>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Button 
            title="push" 
            onPress={() => navigation.navigate('Robot', {direction: 'eject'})}
          />
        </View>
      </View>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Button 
            title="Right" 
            onPress={() => navigation.navigate('Robot', {direction: 'right'})}
          />
        </View>
      </View>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Button 
            title="Scan" 
            onPress={() => navigation.navigate('Camera')}
          />
        </View>
      </View>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Button 
            title="Start"
            onPress={() => navigation.navigate('Robot', {direction: 'start'})}
          />
        </View>
      </View>
      <View style={styles.box}>
        <View style={styles.inner}>
          <Button 
            title='Stop'
            onPress={() => navigation.navigate('Robot', {direction: 'stop'})}
          />
        </View>
      </View>
    </View>
  );
};

export default Boxes;

const styles = StyleSheet.create({
  container: {
    width: '100%',
    height: '85%',
    padding: 5,
    flexDirection: 'row',
    flexWrap: 'wrap'
  },
  box: {
    width: '33%',
    height: '50%',
    padding: 5
  },
  inner: {
    flex: 1,
    backgroundColor: '#eee',
    alignItems: 'center',
    justifyContent: 'center'
  }
})
