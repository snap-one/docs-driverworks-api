
## Receiver with Onscreen Binding

To enable a receiver to be capable of being the onscreen device, add the following to your \<connections\> section of your driver.  This will then allow the room's onscreen input to be hooked up to the receiver’s output.  Note that for the sections to be valid, a video path must also exist (the room must also be able to select the receiver as the video endpoint).

### Example

```lua
<connection>
    <id>7500</id>
    <facing>6</facing>
    <connectionname>OnscreenNavigator</connectionname>
    <type>7</type>
    <consumer>False</consumer>
    <audiosource>False</audiosource>
    <videosource>False</videosource>
    <linelevel>False</linelevel>
   <classes>
    <class>
      <classname>ONSCREEN_SELECTION</classname>
    </class>
  </classes>
</connection>
```



