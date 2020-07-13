## Introduction

The Controller Registry APIs enables drivers to set, retrieve, and delete values that are stored in the Registry. The Registry consists of a database table stored in: /opt/control4/etc/registry.db.

The Registry associates a value with a well-known key. The registry is intended to store values that are global in nature. The Registry would be a good place for storing configuration data that pertains to all instances of a particular driver. Drivers SHOULD NOT use the registry to store state, or other data that are transient in nature.

The Registry APIs utilizes the same encoder/decoder used by the JSON APIs for Lua.  Drivers using these APIs can persist numbers, strings, booleans, or tables. When retrieved, values are decoded back into the original type.