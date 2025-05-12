"""Base configuration for LangGraph applications."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, Optional, Type, TypeVar

from langchain_core.runnables import RunnableConfig

T = TypeVar("T", bound="BaseConfiguration")

@dataclass(kw_only=True)
class BaseConfiguration:
    """Base configuration class for LangGraph applications.
    
    This class provides common functionality for all configuration classes
    in the application, including methods for converting to and from
    RunnableConfig objects.
    """
    
    CONFIG_KEY: ClassVar[str] = "configurable"
    
    @classmethod
    def from_runnable_config(cls: Type[T], config: RunnableConfig) -> T:
        """Create a configuration instance from a RunnableConfig.
        
        Args:
            config: The RunnableConfig object to extract configuration from.
            
        Returns:
            A new instance of the configuration class.
        """
        if cls.CONFIG_KEY in config:
            config_params = config[cls.CONFIG_KEY]
            if isinstance(config_params, dict):
                # Filter to include only keys that are valid for this dataclass
                valid_params = {k: v for k, v in config_params.items() 
                                if k in cls.__dataclass_fields__}
                return cls(**valid_params)
        
        # Return default instance if no config found
        return cls()
    
    def to_runnable_config(self) -> RunnableConfig:
        """Convert this configuration to a RunnableConfig.
        
        Returns:
            A RunnableConfig object containing this configuration.
        """
        return {self.CONFIG_KEY: {k: v for k, v in self.__dict__.items()}} 